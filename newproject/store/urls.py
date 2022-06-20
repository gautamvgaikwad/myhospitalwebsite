from django.urls import path
from .views import ecomview


urlpatterns =[
    path('ecom/', ecomview, name='ecom'),
 ]