from django.db import models

# Create your models here.

class Product(models.Model):
    name = models.CharField(max_length=50)
    price = models.DecimalField(max_digits = 10, decimal_places = 2)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add = True)



class Customer(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length = 20) 



class Order(models.Model):
    order_date = models.DateTimeField(auto_now_add = True)
    customer = models.ForeignKey(Customer, on_delete = models.CASCADE)
    
