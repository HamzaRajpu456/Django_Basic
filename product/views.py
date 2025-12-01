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
    # return HttpResponse("<h1> Hello From Home! </h1>")

# render django templates: 
    return render(HttpResponse, "home.html", {})



def contact_view(request):
    # return HttpResponse("<h1> Welcome to Contact Page!</h1>")
   
   return render(HttpResponse, "contact.html", {})



def about_view(request):
    # return HttpResponse("<h1> Welcome to About Page!</h1>")   
    
    return render(HttpResponse, "about.html", {})






# CBV = Views written using Python classes instead of functions.

def HomeView():
    def get(self, request):
        return HttpResponse("This is GET request")
    
# CRUD Using Class_Based Viws:
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator



from django.views import View
from django.http import JsonResponse
from .models import Product
import json

# Add CSRF for testing in Postman: cross-sight 
@method_decorator(csrf_exempt, name="dispatch")
# Create product :

class ProductCreateView(View):
    def post(self,request):
        body = json.loads(request.body)
        product = Product.objects.create(
        
            name = body['name'],
            price = body['price'],
            description = body['description']
        ) 

        return JsonResponse({"message": "product Created Successfully!", "id":product.id})

# Get ALL Products :
class ProductListView(View):
    def get(self, request):
        products = list(Product.objects.values())

        return JsonResponse({"All Products" : products}) 


# Get Product By ID :
class ProductDetailView(View):
    def get(self, request, id):

        product = Product.objects.filter(id=id).first()

        if not product:
            return JsonResponse({"Error": "Product Not Found!"})
        
        data = {
            "id"   : product.id,
            "name" : product.name,
            "price": product.price,
            "description": product.description 
        }
        # print(data)
        return JsonResponse(data)
    

# Update Product :
@method_decorator(csrf_exempt, name="dispatch")
class ProductUpdateView(View):
    def put(self, request, id):

        product = Product.objects.filter(id=id).first()
        
        if not product:
            return JsonResponse({"Error": "Product Not Found! Enter a valid ID"}, status=404)

        body = json.loads(request.body)

        product.name = body.get('name', product.name)
        product.price = body.get('price', product.price)
        product.description = body.get('description', product.description)

        product.save()
        return JsonResponse({"Message": "Product Updated Successfully!"})
    
# Delete Product :

class DeleteProductView(View):
    def delete(self, request, id):
        product = Product.objects.filter(id=id).first()

        if not product:
            return JsonResponse({"Error": "Product Not found! Enter Valid ID"})

        product.delete()
        return JsonResponse({"Message": "Product Deleted!"})
