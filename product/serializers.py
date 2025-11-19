from rest_framework import serializers
from .models import Product, Customer, Order

# serializer : convert Product/Model to JSON

class ProductSerializer(serializers.Serializer):

    class Meta:
        model = Product
        fields = "__all__"



class CustomerSerializer(serializers.Serializer):

    class Meta : 
        model = Customer
        fields = "__all__"


class OrderSerializer(serializers.Serializer):

    class Meta:
        model = Order
        fields = "__all__"
