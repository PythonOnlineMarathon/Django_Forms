
from django.urls import path
from book import views



urlpatterns = [
    path('', views.index, name='books'),
    path('new', views.create_book, name='create_book'),
    path('update_book/<int:pk>/', views.update_book, name='update_book'),
    path('delete_book/<int:pk>/', views.delete_book, name='delete_book'),
    path('books_by_author/<int:id>/', views.books_by_author, name='books_by_author'),
    path('orders/', views.orders, name='orders'),
    path('users/', views.users, name='users'),
    path('books_by_user/<int:id>/', views.books_by_user, name='books_by_user'),
    path('asc_name/', views.asc_name, name='asc_name'),
    path('desc_name/', views.desc_name, name='desc_name'),
    path('asc_count/', views.asc_count, name='asc_count'),
    path('desc_count/', views.desc_count, name='desc_count'),
    path('overdue_users/', views.overdue_users, name='overdue_users'),
    path('books/',  views.all_books_filter, name='list_books'),
    path('books/<book_pk>/', views.book_description, name='book_description'),
    path('available_books/', views.available_books, name='available_books'),
] 

