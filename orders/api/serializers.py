from rest_framework import serializers
from orders.models import Order
from shop.models import Product

class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ('first_name','last_name','email')

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model= Product
        fields=('name','description','price')

