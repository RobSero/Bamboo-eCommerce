from django.shortcuts import render

# Create your views here.
def cart_home(req):
  return render(req, 'carts/home.html', {})