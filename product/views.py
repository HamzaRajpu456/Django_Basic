from django.shortcuts import render
from django.http import HttpResponse
from django.views import View


"""A View is just a function or class that receives an HTTP request and returns a response.
 Types:
 1.Function-Based Views (FBV)
 2.Class-Based Views (CBV)"""


# Create your views here.
# FBV = Views written using normal Python functions.

def home():
    return {"meassage": "Welcome to Homepage!"}

def home_view(*args, **kwargs):
    return HttpResponse("<h1>Hello From View!</h1>")
# CBV = Views written using Python classes instead of functions.

# def HomeView():
#     def get(self, request):
#         return HttpResponse("This is GET request")
    