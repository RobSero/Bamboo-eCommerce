from django.shortcuts import render,redirect
from .models import Watchlist
from products.models import Product
# Create your views here.


def update_watchlist(req, product_id):
  # check if user is signed in, send to login if not
  if not req.user.is_authenticated:
    return redirect('login')
  # get_or_create Watchlist by user
  watchlist_obj = Watchlist.objects.get_or_create(user=req.user)
  # get Product
  # check if product is in Watchlist object
  # toggle in the watchlist
  print(product_id)
  return redirect('list')