from django.conf.urls import url
from . import views

urlpatterns=[
    url(r'^order/$',views.OrderListView.as_view(),name='order_list'),
    url(r'^order/(?P<pk>\d+)/$',views.OrderDetailView.as_view(),name='order_detail'),
    url(r'^product/$',views.ProductListView.as_view(),name='product_list'),
    url(r'^product/(?P<pk>\d+)/$',views.ProductDetailView.as_view(),name='product_detail'),

]