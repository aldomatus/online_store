"""Views of my projet"""
#   Django 
from django.shortcuts import render, HttpResponse

#   views
def home(request):
    
    return render(request,"online_store_app/home.html")


def store(request):
    
    return render(request,"online_store_app/store.html")

def blog(request):
    
    return render(request,"online_store_app/blog.html")

def contact(request):
    
    return render(request,"online_store_app/contact.html")



