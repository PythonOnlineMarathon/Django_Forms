from django.urls import path
from . import views

urlpatterns = [

    path('', views.authors, name='authors'),
    path('new', views.create_author, name='create_author'),
    path('update_author/<int:pk>/', views.update_author, name='update_author'),
    path('delete_author/<int:pk>/', views.delete_author, name='delete_author'),
    ]