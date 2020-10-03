from django.shortcuts import render, redirect
from .models import Cart
from products.models import Product
from order.models import Order
from accounts.forms import LoginForm
from billing.models import BillingProfile

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
  billing_profile = None
  if user.is_authenticated:
    billing_profile = BillingProfile.objects.get_or_create(user=user, email=user.email)
  login_form = LoginForm()
  context = {
    'object' : order,
    'billing_profile' : billing_profile,
    'cart' : cart,
    'login_form' : login_form
  }
  return render(req, 'carts/checkout.html', context)