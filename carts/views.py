from django.shortcuts import render, redirect
from .models import Cart


# Create your views here.
def cart_home(req):
  cart = Cart.objects.new_cart_or_get(req)  
  return render(req, 'carts/home.html', {})