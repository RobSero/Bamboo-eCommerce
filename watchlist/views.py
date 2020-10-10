from django.shortcuts import render,redirect
from django.http import JsonResponse
from .models import Watchlist
from products.models import Product

# Create your views here.


def update_watchlist(req, product_id):
  
  # check if user is signed in, send to login if not
  if not req.user.is_authenticated:
    return redirect('login')
  # get_or_create Watchlist by user
  watchlist_obj,new_watchlist = Watchlist.objects.get_or_create(user=req.user)
  # get Product
  product_obj = Product.objects.get(id=product_id)
  # toggle product in cart
  if product_obj in watchlist_obj.products.all():
    watchlist_obj.products.remove(product_obj)
    added = False
  else:
    watchlist_obj.products.add(product_obj)
    added = True
  req.session['watchlist_items'] = watchlist_obj.products.count()
  if req.is_ajax():
    print('ajax request')
    return JsonResponse({'added' : added, 'watchlist_length' : watchlist_obj.products.count() })
  redirect('list')


def watchlist(req):
  # check if user is signed in, send to login if not
  if not req.user.is_authenticated:
    return redirect('login')
  # get_or_create Watchlist by user
  watchlist_obj,new_watchlist = Watchlist.objects.get_or_create(user=req.user)
  print('YO')
  return render(req, 'watchlist/watchlist.html', {'watchlist': watchlist_obj})