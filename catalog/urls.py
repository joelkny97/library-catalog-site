from django.urls import path, re_path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('books/', views.BookListView.as_view(), name='books'),
    # re_path(r'^book/(?P<stub>[-\w]+)$', views.BookDetailView.as_view(), name='book-detail'),
    path('book/<slug:slug>', views.BookDetailView.as_view(), name='book-detail'),
    path('authors/', views.AuthorListView.as_view(), name='authors'),
    path('author/<slug:slug>', views.AuthorDetailView.as_view(), name='author-detail'),
    path('mybooks/', views.LoanBooksByUserListView.as_view(), name='my-borrowed'),
    path('loanedbooks/', views.LoanBooksByUserLibrariansListView.as_view(), name='users-borrowed'),
    path('book/<uuid:pk>/renew/', views.renew_book_librarian, name='renew-book-librarian'),
]

# path('author/<int:pk>', views.AuthorDetailView.as_view(), name='author-detail'),
