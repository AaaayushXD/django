from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
#first try
def index(request): 
    return render(request, "hello/index.html")

#use string
def greet(request, name):
    return render(request, "hello/greet.html", {
        "name": name.capitalize()
    })