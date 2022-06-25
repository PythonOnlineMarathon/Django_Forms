from django.conf.urls import url
from django.urls import path
from . import views

urlpatterns = [
    url(r'^$', views.order_list, name='order_list'),    
    path(r'create/<int:pk>/', views.order_create, name='order_create'),
    path('delete/<int:pk>/', views.order_delete, name='order_delete'),
    path('update/<int:pk>/', views.order_update, name='order_update'),
    path('return/<int:pk>/', views.order_return, name='order_return')
]

