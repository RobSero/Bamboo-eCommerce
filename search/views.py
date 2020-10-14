from django.db.models import Q
from django.shortcuts import render
from django.views.generic import ListView
from products.models import Product


class SearchProductView(ListView):
  queryset = Product.objects.all()
  template_name = 'products/list.html'
  
  def get_queryset(self, *args, **kwargs):
    request = self.request
    search_query = request.GET.get('q', None)
    if search_query is not None:
      return Product.objects.search(search_query) 
    return Product.objects.all()