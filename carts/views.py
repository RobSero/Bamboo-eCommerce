from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Cart

from accounts.forms import LoginForm
from address.forms import AddressForm
from address.models import Address
from order.models import Order
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


def checkout_home(req):
  cart, new_cart = Cart.objects.new_cart_or_get(req)
  if new_cart or cart.products.count() == 0:
    return redirect('carthome')
  order, new_order = Order.objects.get_or_create(cart=cart)
  user = req.user
  login_form = LoginForm()
  user_address, new_address = Address.objects.get_or_create(user=user)
  address_form = AddressForm(instance=user_address)
  context = {
    'object' : order,
    'cart' : cart,
    'login_form' : login_form,
    'address_form' : address_form
  }
  return render(req, 'carts/checkout.html', context)


def set_address(req):
  user = req.user
  address_obj = Address.objects.get(user=user)
  address_form = AddressForm(req.POST, instance=address_obj)
  if address_form.is_valid():
    address_form.save()
    messages.success(req, 'Profile details updated.')
    
  return redirect('checkout')
