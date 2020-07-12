from django.contrib import admin

# Register your models here.

from .models import Author, Genre, Book, BookInstance, Language

#admin.site.register(Book)
#admin.site.register(Author)
admin.site.register(Genre)
#admin.site.register(BookInstance)
admin.site.register(Language)

class BookInline(admin.TabularInline):
    model = Book

class AuthorAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('firstname', 'lastname')}
    list_display = ('lastname','firstname','date_of_birth','date_of_death',)
    fields = ['firstname', 'lastname', ('date_of_birth', 'date_of_death'),'slug',]
    inlines = [BookInline]


admin.site.register(Author,AuthorAdmin)

class BookInstanceInline(admin.TabularInline):
    model = BookInstance

# Register the Admin classes for Book using the decorator
@admin.register(Book)	

class BookAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',),}
    list_display = ('title','author','display_genre',)
    inlines = [BookInstanceInline]

# Register the Admin classes for BookInstance using the decorator
@admin.register(BookInstance) 
class BookInstanceAdmin(admin.ModelAdmin):
    list_display = ('book', 'bk_id', 'status', 'borrower','due_back')
    list_filter = ('status', 'due_back')
    fieldsets = (
        (None, {
            'fields': ('book', 'imprint', 'bk_id')
        }),
        ('Availability', {
            'fields': ('status', 'due_back','borrower')
        }),
    )

