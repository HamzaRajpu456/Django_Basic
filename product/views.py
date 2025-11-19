from django.shortcuts import render
from django.http import HttpResponse


"""A View is just a function or class that receives an HTTP request and returns a response.
 Types:
 1.Function-Based Views (FBV)
 2.Class-Based Views (CBV)"""


# Create your views here.
# FBV = Views written using normal Python functions.

def home():
    return {"meassage": "Welcome to Homepage!"}


# Change Default page to Custom Page:

def home_view(request):
    # print(request)
    return HttpResponse("<h1> Hello From Home! </h1>")


def contact_view(request):
    return HttpResponse("<h1> Welcome to Contact Page!</h1>")
   
def about_view(reuest):
    return HttpResponse("<h1> Welcome to About Page!</h1>")   







# CBV = Views written using Python classes instead of functions.

def HomeView():
    def get(self, request):
        return HttpResponse("This is GET request")
    