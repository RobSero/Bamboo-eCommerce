from django.db import models
from django.db.models import Q
import random
import os
from django.urls import reverse


def upload_image_path(instance, filename):
  new_filename = random.randint(1,200000)
  base_name = os.path.basename(filename)
  name, ext = os.path.splitext(base_name)
  final_filename = f'products/{new_filename}/{new_filename}{ext}'
  return final_filename


#  --- CREATE METHODS TO BE USED ON THE get_queryset METHOD
class ProductQuerySet(models.query.QuerySet):
  def featured(self):  # creates the method: get_queryset().featured()
    return self.filter(featured=True)
  
  def active(self):  # creates the method: get_queryset().active()
    return self.filter(active=True)


# --- CREATES METHODS THAT CAN BE USED ON THE Product.objects METHOD
class ProductManager(models.Manager):
  def get_queryset(self):
    return ProductQuerySet(self.model, using=self._db)
  
  def get_by_id(self, id):
    return self.get_queryset().filter(id=id) # Product.objects == self.get_queryset()
  
  def active(self):
    return self.get_queryset().active()
  
  def feature(self):  # allows for the use of Product.objects.feature()
    return self.get_queryset().featured()
  
  def search(self, query):
    lookup = Q(title__icontains=query) | Q(description__icontains=query) | Q(tag__title__icontains=query) 
    return self.get_queryset().filter(lookup).active().distinct() # distinct stops the same item being shown twice if it matches both Q statements





class Product(models.Model):
  title = models.CharField(max_length=100)
  slug = models.SlugField(default='abc', unique=True)
  description = models.TextField()
  price = models.DecimalField(decimal_places=2, max_digits=10, default=0.99)
  image = models.ImageField(upload_to=upload_image_path, null=True, blank=True)
  image1 = models.ImageField(upload_to=upload_image_path, null=True, blank=True)
  image2 = models.ImageField(upload_to=upload_image_path, null=True, blank=True)
  image3 = models.ImageField(upload_to=upload_image_path, null=True, blank=True)
  image4 = models.ImageField(upload_to=upload_image_path, null=True, blank=True)
  featured = models.BooleanField(default=False)
  active = models.BooleanField(default=True)
  measurements = models.CharField(max_length=50, default='N/A')
  material = models.CharField(max_length=50, default='N/A')
  condition = models.CharField(max_length=50, default='N/A')
  
  @property
  def name(self):
    return self.title
  
  
  objects = ProductManager()
  
  def get_absolute_url(self):
      return reverse("productdetail", kwargs={"slug": self.slug})
  
  
  
  def __str__(self):
    return f'{self.title} - Product'


