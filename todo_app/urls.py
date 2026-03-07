from django.urls import path
from .views import *

urlpatterns = [
    path('',home,name='home'),
    path('add/',add,name='add'),
    path('complete/',complete,name='complete'),
    path('trash/',trash,name='trash'),
    path('about/',about,name='about'),
    path('completed/<int:id>/',completed,name='completed'),
    path('delete/<int:id>/',delete,name='delete'),
    path('restore/<int:id>/',restore,name='restore'),
    path('complete_all/',complete_all,name='complete_all'),
    path('delete_all/',delete_all,name='delete_all')

]