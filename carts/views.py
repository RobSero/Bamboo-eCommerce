from django.shortcuts import render, redirect
from .models import Cart
from products.models import Product


# Create your views here.
def cart_home(req):
  cart , new_cart = Cart.objects.new_cart_or_get(req)  
  return render(req, 'carts/home.html', {'cart':cart})



def cart_update(req):
  product_id = req.POST.get('product_id')
  if product_id != None:
    try:
      product = Product.objects.get(id=product_id)
    except product.DoesNotExist:
      return redirect('carthome')
    cart, new_cart = Cart.objects.new_cart_or_get(req)
    if product in cart.products.all():
      cart.products.remove(product)
    else:
      cart.products.add(product)
  req.session['cart_items'] = cart.products.count()   
  return redirect('carthome')