from django.urls import path
from .views import *

urlpatterns = [
    path('',login_,name='login'),
    path('register/',register,name='register'),
    path('profile/',profile,name='profile'),
    path('logout/',logout_,name='logout'),
]