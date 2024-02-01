from django.urls import path
from core.views import index
from core import views

urlpatterns=[
    path('index/',views.index,name="index"),
    path('cart/',views.cart,name="cart"),
    path('checkout/',views.checkout,name="checkout"),
    path('contact/',views.contact,name="contact"),
    path('shopdetail/',views.shopdetail,name="shopdetail"),
    path('shop/',views.shop,name="shop"),
    path('testimonial/',views.testimonial,name="testimonial"),

]