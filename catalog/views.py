from django.shortcuts import render, get_object_or_404
from django.db.models import Max, Count
from django.views import generic
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import permission_required
import datetime
from django.http import HttpResponseRedirect
from django.urls import reverse
from catalog.forms import RenewBookForm

# Create your views here.
from catalog.models import Book, BookInstance, Author, Genre, Language

@login_required
def index(request):
    """View function for home page"""

    #Number of visits to this view
    num_visits = request.session.get('num_visits', 0)
    request.session['num_visits'] = num_visits + 1

    #Generate counts of various objects
    num_books = Book.objects.all().count()
    num_book_instances = BookInstance.objects.all().count()

    #available books
    num_instances_available = BookInstance.objects.filter(status__exact='a').count()

    num_authors = Author.objects.all().count()

    #most borrowed books
    max_book_count = BookInstance.objects.values('book__title').annotate(num_inst=Count('book__id')).order_by('-num_inst')[0]
    if BookInstance.objects.all().count() != 0:
        most_borrowed = max_book_count['book__title']
    else:
        most_borrowed = 'None'

    #title search - the
    titles_with_game = Book.objects.filter(title__icontains='game')

    #context dictionary to pass to template
    context = {
        'num_books': num_books,
        'num_book_instances': num_book_instances,
        'num_instances_available': num_instances_available,
        'num_authors': num_authors,
        'most_borrowed': most_borrowed,
        'titles_with_game': titles_with_game,
        'num_visits': num_visits,
    }

    return render(request, 'index.html', context=context)

#class view to generate list view of all books
class BookListView(LoginRequiredMixin,generic.ListView):
    login_url = '/accounts/login/'
    redirect_url = 'catalog/'
    model = Book
    pagination = 10
    paginate_by = 2
    #context_object_name = 'my_book_list' #custom name for list as template variable
    template_name = 'catalog/book_list.html' #custom template file

    def get_queryset(self):
        return Book.objects.all()   #return 5 books in list view

    def get_context_data(self, **kwargs):
        #call base implementation first to get context
        context = super(BookListView, self).get_context_data(**kwargs)

        #creating some custom data to be added
        context['some_data'] = 'some data'
        return context
class BookDetailView(LoginRequiredMixin,generic.DetailView):
    login_url = '/accounts/login/'
    redirect_url = 'catalog/'
    model = Book
    template_name = 'catalog/book_detail.html'  # custom template file

#class view to generate list view of all authors
class AuthorListView(LoginRequiredMixin,generic.ListView):
    login_url = '/accounts/login/'
    redirect_url = 'catalog/'
    model = Author
    # query_pk_and_slug = True
    pagination = 10
    #context_object_name = 'my_book_list' #custom name for list as template variable
    template_name = 'catalog/author_list.html' #custom template file

    def get_queryset(self):
        return Author.objects.all()  #return 5 books in list view

    def get_context_data(self, **kwargs):
        # call base implementation first to get context
        context = super(AuthorListView, self).get_context_data(**kwargs)

        # creating some custom data to be added
        context['some_data'] = 'some data'
        return context


class AuthorDetailView(LoginRequiredMixin,generic.DetailView):
    login_url = '/accounts/login/'
    redirect_url = 'catalog/'
    model = Author
    template_name = 'catalog/author_detail.html'
    #query_pk_and_slug = True  # calling pk and slug


class LoanBooksByUserListView(LoginRequiredMixin,generic.ListView):
    """Generic class-based view listing all loaned books by current user"""
    model = BookInstance
    template_name = 'catalog/book_instance_list_borrowed_user.html'
    paginate_by = 10
    def get_queryset(self):
        return BookInstance.objects.filter(borrower=self.request.user).filter(status__exact = 'o').order_by('due_back')

class LoanBooksByUserLibrariansListView(LoginRequiredMixin,generic.ListView):
    """Generic class-based view listing all loaned books by all users to display to librarains"""
    model=BookInstance
    permission_required = 'catalog.can_mark_returned'
    template_name='catalog/book_instance_list_borrowed_librarian.html'
    paginate_by = 10
    def get_queryset(self):
        return BookInstance.objects.filter(status__exact = 'o').order_by('due_back')

@permission_required('catalog.can_renew')
def renew_book_librarian(request, pk):
    book_instance = get_object_or_404(BookInstance, pk=pk)

    # If this is a POST request then process the Form data
    if request.method == 'POST':
        # Create a form instance and populate it with data from the request (binding)
        form = RenewBookForm(request.POST)

        #check if form is valid
        if form.is_valid():
            #process the data in form.cleaned_data as required (here we just write to model due_back)
            book_instance.due_back = form.cleaned_data['renewal_date']
            book_instance.save()

            #redirect to new url after date is set
            return HttpResponseRedirect(reverse('users-borrowed'))

    #If this a GET or any other method, display initial default form
    else:
        proposed_renewal_date = datetime.date.today() + datetime.timedelta(weeks=3)

        form = RenewBookForm(initial={'renewal_date': proposed_renewal_date})


    context = {
        'form': form,
        'book_instance': book_instance,
    }

    return render(request, 'catalog/book_renew_librarian.html', context)







