from django.shortcuts import render

# Create your views here.
def payment_page(req):
  return render(req,'carts/paymentpage.html', {})


def charge_card(req):
  if req.method == 'POST':
    print(req.POST)
  return render(req,'carts/paymentpage.html', {})