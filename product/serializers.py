from rest_framework import serializers
from .models import Product, Customer, Order

# serializer : 
# convert Product/Model to JSON
# JSON To --> Model

class ProductSerializer(serializers.ModelSerializer):

    class Meta:
        model = Product
        fields = "__all__"



class CustomerSerializer(serializers.ModelSerializer):

    class Meta : 
        model = Customer
        fields = "__all__"


class OrderSerializer(serializers.ModelSerializer):

    class Meta:
        model = Order
        fields = "__all__"
