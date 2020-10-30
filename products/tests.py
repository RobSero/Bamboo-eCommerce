from django.test import TestCase
from .models import Product

class ProductTestSuite(TestCase):
  def setUp(self):
    Product.objects.create(title='testProduct', slug='sluggage', description='nice new test products for sale', price=3.25)
    Product.objects.create(title='Piri Piri Banana', slug='piri', description='tasty potassium', price=2.00)
    Product.objects.create(title='Apples', slug='yummypiri', description='tasty piri cyanide', price=2.00)
    
    
  def test_get_product(self):
    new_product = Product.objects.get(title='testProduct')
    self.assertEqual(new_product.price, 3.25)
    self.assertEqual(new_product.slug, 'sluggage')
    
  def test_search_queries(self):
    empty_search_product_queryset = Product.objects.search('chicken')
    filled_product_queryset = Product.objects.search('piri')
    empty_featured_product_queryset = Product.objects.feature()
    all_products = Product.objects.all()
    
    self.assertFalse(empty_search_product_queryset)
    self.assertTrue(filled_product_queryset)
    self.assertEqual(filled_product_queryset.first().title, 'Piri Piri Banana')
    self.assertEqual(filled_product_queryset.last().title, 'Apples')
    self.assertFalse(empty_featured_product_queryset)
    self.assertEqual(len(all_products), 3)
  


