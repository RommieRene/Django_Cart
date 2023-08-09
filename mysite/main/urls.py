from django.urls import path
from . import views 

urls=[path('', views.home, name = 'home'),
      path('contact/', views.contact, name = 'contact'),
      path('product/<int:id>/', views.contact, name = 'contact'),
      path('product_detail/<slug:slug>/', views.product_detail, name = 'product_detail'),
      ]