from django.shortcuts import render, get_object_or_404, Http404
from .models import Product
from django.views.generic import ListView, DetailView


class ProductListView(ListView):
  queryset = Product.objects.all()
  template_name = 'products/list.html'
  
  def get_context_data(self, *args, **kwargs):
    context = super(ProductListView, self).get_context_data(*args, **kwargs)
    print(context)
    return context
  
  

class ProductFeaturedListView(ListView):
  queryset = Product.objects.all()
  template_name = 'products/list.html'
  
  def get_context_data(self, *args, **kwargs):
    context = super(ProductListView, self).get_context_data(*args, **kwargs)
    print(context)
    return context
  


class ProductDetailView(DetailView):
  template_name = 'products/detail.html'
  queryset = Product.objects.all()
  # def get_context_data(self, *args, **kwargs):
  #   context = super(ProductDetailView, self).get_context_data(*args, **kwargs)
  #   print(context)
  #   return context
  
  def get_queryset(self, *args, **kwargs):
    request = self.request
    pk = self.kwargs.get('pk')
    return Product.objects.get_by_id(pk)




class ProductFeaturedDetailView(DetailView):
  template_name = 'products/detail.html'
  queryset = Product.objects.all()

  def get_queryset(self, *args, **kwargs):
    request = self.request
    pk = self.kwargs.get('pk')
    return Product.objects.get_by_id(pk)