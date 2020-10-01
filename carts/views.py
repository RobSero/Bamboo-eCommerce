from django.shortcuts import render
from .models import Cart

# Create your views here.
def cart_home(req):
  cart_id = req.session.get('cart_id', None)
  if cart_id == None:
    cart = Cart.objects.create(user=None)
    req.session['cart_id'] = cart.id
  else:
    query = Cart.objects.filter(id=cart_id)
    if query.count() == 1:
        cart = query.first()
    else:
        cart = Cart.objects.create(user=None)
    req.session['cart_id'] = cart.id
  
  return render(req, 'carts/home.html', {})