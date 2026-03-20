from django.urls import path
from .views import *
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),      
    path('service/', views.service, name='service'),
    path('price/', views.price, name='price'),    
    path('team/', views.team, name='team'),        
    path('appointment/', views.appointment, name='appointment'),
    path('contact/', views.contact, name='contact'),
    path('gallery/', views.gallery, name='gallery'),
]