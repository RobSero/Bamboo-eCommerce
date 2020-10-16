from django.shortcuts import render
from django.contrib.auth import get_user_model
import stripe

User = get_user_model()
# Create your views here.
def payment_page(req):
  return render(req,'carts/paymentpage.html', {})


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