from django.db import models
import uuid
import datetime
from django.urls import reverse
from django.utils.text import slugify
from django.conf import settings


# from django.core.validators import MaxValueValidator, MinValueValidator

# year Validators

def max_year_current(value):
	return MaxValueValidator(datetime.date.today().year)(value)


# Create your models here.

class Book(models.Model):
	"""A typical class defining a model, derived from the Model class."""

    # Fields
	title = models.CharField(max_length=200)

    #foreign key field on Author with M:1 relationship
	author = models.ForeignKey('Author', on_delete=models.SET_NULL, null=True)
	isbn = models.CharField('ISBN', max_length=13, help_text='13 character ISBN of book <a href="https://www.isbn-international.org/content/what-isbn">ISBN number</a>')

	summary = models.TextField(max_length=1000, help_text='Enter a brief description of the book')

    # ManyToManyField used because genre can contain many books. Books can cover many genres.
	genre = models.ManyToManyField('Genre', help_text='Select a genre for this book')

	# ManyToManyField used because lang can contain many books. Books can cover many languages.
	language = models.ManyToManyField('Language', help_text='Enter a language for this book')


	published_date = models.DateField('Published Date',null=True,blank=True,help_text='Enter published date for this book')

	def display_genre(self):
		"""Create a string for the Genre. This is required to display genre in Admin."""
		return ', '.join(genre.name for genre in self.genre.all()[:3])
	def display_lang(self):
		"""Create a string for the language. This is required to display language in Admin."""
		return ', '.join(language.name for language in self.language.all())

	display_genre.short_desciption = 'Genre'
	display_lang.short_desciption = 'Language'
	#field for maintaining multiple copies of a single book in Library
	#available_count = models.IntegerField(default=1)

    # Metadata
	class Meta: 
		ordering = ['title','author']
	# Methods
	def get_absolute_url(self):
		"""Returns the url to access a particular instance of MyModelName."""
		return reverse('book-detail', args=[str(self.id)])
	def __str__(self):
		"""String for representing the MyModelName object (in Admin site etc.)."""
		return self.title

class Language(models.Model):
	"""Model representing book language"""
	name = models.CharField(max_length=100, help_text='Enter a book language')

	def __str__(self):
		"""String for representing the Model object."""
		return self.name



class Genre(models.Model):
	"""Model representing a book genre."""
	name = models.CharField(max_length=200, help_text='Enter a book genre (e.g. Science Fiction)')

	def __str__(self):
		"""String for representing the Model object."""
		return self.name


class BookInstance(models.Model):
	"""Model representing a specific copy of a book (i.e. that can be borrowed from the library)."""
	bk_id = models.UUIDField(primary_key=True, default=uuid.uuid4, help_text='Unique ID for this book across whole library')
	book = models.ForeignKey('Book', on_delete=models.SET_NULL, null=True)
	imprint = models.CharField(max_length=200)
	due_back = models.DateField(null=True,blank=True)

	LOAN_STATUS = (
		('m','Maintenance'),
		('o','On loan'),
		('a','Available'),
		('r','Reserved'),
		)
	status = models.CharField(max_length=1,choices=LOAN_STATUS,blank=True,default='m',help_text='Book availability')

	class Meta:
		ordering = ['due_back']

	"""String for representing the Model object."""	
	def __str__(self):
		return '{0} ({1})'.format(self.bk_id,self.book.title)
	def get_status_display(self):
		if self.status == 'a':
			return 'Available'
		elif self.status == 'm':
			return 'Maintenance'
		elif self.status == 'o':
			return 'On loan'
		elif self.status == 'r':
			return 'Reserved'



class Author(models.Model):

	#Fields 
	firstname = models.CharField(max_length=100, help_text='Enter Author\'s first name')
	lastname = models.CharField(max_length=100, help_text='Enter Author\'s last name')
	date_of_birth = models.DateField(null=True,blank=True)
	date_of_death = models.DateField('Died', null=True, blank=True)

	class Meta:
		ordering = ['lastname', 'firstname']

	def get_absolute_url(self):
		"""Returns the url to access a particular author instance."""
		return reverse('author-detail', args=[str(self.id)])

	def __str__(self):
		"""String for representing the Model object."""
		return '{0}, {1}'.format(self.firstname, self.lastname)
