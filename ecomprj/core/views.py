from django.shortcuts import render
from django.http import HttpResponse
def index(request):
    return render(request,"index.html")
def cart(request):
    return render(request,"cart.html")
def checkout(request):
    return render|(request,"checkout.html")
def contact(request):
    return render(request,"contact.html")
def shopdetail(request):
    return render(request,"shop-detail.html")
def shop(request):
    return render(request,"shop.html")
def testimonial(request):
    return render(request,"testimonial.html")
