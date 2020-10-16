from django.shortcuts import render
from django.contrib.auth import get_user_model



from carts.models import Cart
from accounts.forms import LoginForm
from address.forms import AddressForm
from address.models import Address
from order.models import Order
from products.models import Product
import stripe

User = get_user_model()
# Create your views here.
def payment_page(req):
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
  return render(req,'carts/paymentpage.html', context)


def charge_card(req):
  user = req.user
  if req.method == 'POST':
    print(req.POST)
    print(user.full_name)
    customer = stripe.Customer.create(
      name= user.full_name,
      email = user.email,
      source = req.POST['stripeToken']
    )
    charge = stripe.Charge.create(
      customer=customer,
      amount=5000,
      currency='gbp',
      description='bamboo payment'
    )
  return render(req,'carts/paymentpage.html', {})