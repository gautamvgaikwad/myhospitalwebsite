from django.urls import path, include
from django.contrib import admin
from . import views

urlpatterns = [
    path('home/', views.homeview, name='home'),
    path('appointment/', views.appointmentview, name='appointment'),
    path('ambulance/', views.ambulanceview, name='ambulance'),
    path('about/', views.aboutview, name='about'),
    path('login/', views.loginview, name='login'),
    path('logout/', views.logoutview, name='logout'),
    path('reg/', views.registerview, name='register'),
    path('ecommerce/', views.ecomview, name='ecom')


]
