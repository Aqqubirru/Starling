from multiprocessing import context
from turtle import title
from django.shortcuts import render,HttpResponse

# Create your views here.
def awal(request):
    return HttpResponse('Selamat datang di Starling')
    

def home(request):
    context={
        'title':title
    }
    return render(request, 'home.html',context)

def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')

def list(request):
    return render(request, 'list.html')

def menu(request):
    return render(request, 'menu.html')