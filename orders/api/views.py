from rest_framework import generics
from orders.models import Order
from .serializers import OrderSerializer,ProductSerializer
from shop.models import Product

class OrderListView(generics.ListAPIView):
    queryset=Order.objects.all()
    serializer_class = OrderSerializer

class OrderDetailView(generics.RetrieveAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

class ProductListView(generics.ListAPIView):
    queryset=Product.objects.all()
    serializer_class = ProductSerializer

class ProductDetailView(generics.RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

