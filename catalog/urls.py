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
    path('bookinst/create/', views.BookInstanceCreate.as_view(), name='bookinstance_create'),
    path('bookinst/<uuid:pk>/update/', views.BookInstanceUpdate.as_view(), name='bookinstance_update'),
    path('bookinst/<uuid:pk>/delete/', views.BookInstanceDelete.as_view(), name='bookinstance_delete'),
    path('librarian/manage/', views.LibrariansManageListView.as_view(), name='librarian_manage'),
    path('author/create/', views.AuthorCreate.as_view(), name='author_create'),
    path('author/<slug:slug>/update/', views.AuthorUpdate.as_view(), name='author_update'),
    path('author/<slug:slug>/delete/', views.AuthorDelete.as_view(), name='author_delete'),
    path('book/create/', views.BookCreate.as_view(), name='book_create'),
    path('book/<slug:slug>/update/', views.BookUpdate.as_view(), name='book_update'),
    path('book/<slug:slug>/delete/', views.BookDelete.as_view(), name='book_delete'),
]

# path('author/<int:pk>', views.AuthorDetailView.as_view(), name='author-detail'),
