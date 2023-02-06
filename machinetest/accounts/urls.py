from django.urls import path
from .views import *



urlpatterns = [
    path('signin/',signin,name='login'),
    path('list/',listofapplication,name='list'),
    path('logout/',logoutadmin,name='logout'),
]
