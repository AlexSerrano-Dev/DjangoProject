from django.contrib.auth.views import LoginView
from django.shortcuts import render
from django.http import HttpResponse
from users.models import Product


# Create your views here.
def get_user(request):
    return HttpResponse("Hello World")

def inicio(request):
    products = Product.objects.all()
    context = {
        "products":products
    }
    return render(request, "base.html",context=context)

def acerca_de(request):
    return render(request, "acerca_de.html")

def list_products(request):
    products = Product.objects.all()
    return render(request, "products.html",context={"products":products})
