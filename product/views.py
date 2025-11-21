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
<<<<<<< HEAD
    # return HttpResponse("<h1> Hello From Home! </h1>")

# render django templates: 
    return render(HttpResponse, "home.html", {})



def contact_view(request):
    # return HttpResponse("<h1> Welcome to Contact Page!</h1>")
   
   return render(HttpResponse, "contact.html", {})



def about_view(reuest):
    # return HttpResponse("<h1> Welcome to About Page!</h1>")   
    
    return render(HttpResponse, "about.html", {})
=======
    return HttpResponse("<h1> Hello From Home! </h1>")


def contact_view(request):
    return HttpResponse("<h1> Welcome to Contact Page!</h1>")
   
def about_view(reuest):
    return HttpResponse("<h1> Welcome to About Page!</h1>")   
>>>>>>> 67269d3f7a430015d963fb4a14d5818d03787384







# CBV = Views written using Python classes instead of functions.

def HomeView():
    def get(self, request):
        return HttpResponse("This is GET request")
<<<<<<< HEAD
    
# CRUD Using Class_Based Viws:
 
from django.views import View
from django.http import JsonResponse
from .models import Product
import json

class ProductCreateView(View):
    def post(self,request):
        body = json.loads(request.body)
        product = Product.objects.create(
        
            name = body['name'],
            price = body['price'],
            description = body['description']
        ) 
    
        return JsonResponse({"message": "product Created Successfully!", "id":product.id})
     

class ProductListView(View):
    def get(self, request):
        products = list(Product.objects.values())

        return JsonResponse({"All Products" : products}) 


class ProductDetailView(View):
    def get(self, request, id):

        product = Product.objects.filter(Product.id == id).first()

        if not product:
            return JsonResponse({"Error: Product Not Found!"})
        
        data = {
            "id"   : product.id,
            "name" : product.name,
            "price": product.price,
            "description": product.description 
        }
        print(data)
        return JsonResponse(data)
=======
    
>>>>>>> 67269d3f7a430015d963fb4a14d5818d03787384
