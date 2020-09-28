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
  
  def get_queryset(self, *args, **kwargs):
      print('HEEEDHEUD')
      request = self.request
      return Product.objects.feature()
    


class ProductDetailView(DetailView):
  template_name = 'products/detail.html'
  queryset = Product.objects.all()

  def get_queryset(self, *args, **kwargs):
    request = self.request
    pk = self.kwargs.get('pk')
    return Product.objects.get_by_id(pk)



class ProductSlugDetailView(DetailView):
  template_name = 'products/detail.html'
  queryset = Product.objects.all()

  def get_object(self, *args, **kwargs):
        request = self.request
        slug = self.kwargs.get('slug')

        try:
            instance = Product.objects.get(slug=slug, active=True)
        except Product.DoesNotExist:
            raise Http404("Not found..")
        except Product.MultipleObjectsReturned:
            qs = Product.objects.filter(slug=slug, active=True)
            instance = qs.first()
        except:
            raise Http404("Unknown error, please try again")
        return instance




class ProductFeaturedDetailView(DetailView):
  template_name = 'products/detail.html'
  queryset = Product.objects.all()

  def get_queryset(self, *args, **kwargs):
    request = self.request
    pk = self.kwargs.get('pk')
    print('YO')
    return Product.objects.active()