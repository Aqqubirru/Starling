from unicodedata import name
from django.urls import path
from . import views

urlpatterns = [
    path('',views.awal,name='awal'),
    
    path('home/',views.home,name='home'),
    path('about/',views.about,name='about'),
    path('contact/',views.contact,name='contact'),
    path('list/',views.list,name='list'),
    path('menu/',views.menu,name='menu'),
]