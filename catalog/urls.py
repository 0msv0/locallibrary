from django.urls import path
from . import views

app_name = 'catalog'

urlpatterns = [
    path(r'', views.Index.as_view(), name='index'),
    path(r'books/', views.BookListView.as_view(), name='books'),
    path(r'book/(<pk>\d+)', views.BookDetailView.as_view(), name='book-detail'),
    path(r'authors/', views.AuthorListView.as_view(), name='authors'),
    path(r'authors/<pk>/', views.AuthorDetailView.as_view(), name='author_detail'),
    path(r'mybooks/', views.LoanedBooksByUserListView.as_view(), name='my-borrowed'),
    path(r'book/<pk>/renew/', views.renew_book_librarian, name='renew-book-librarian'),
    path(r'author/create/', views.AuthorCreate.as_view(), name='author_create'),
    path(r'author/(<pk>\d+)/update/', views.AuthorUpdate.as_view(), name='author_update'),
    path(r'author/(<pk>\d+)/delete/', views.AuthorDelete.as_view(), name='author_delete'),

]
