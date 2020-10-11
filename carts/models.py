from django.db import models
from django.conf import settings
from products.models import Product
from django.db.models.signals import m2m_changed, pre_save

User = settings.AUTH_USER_MODEL

#  add new methods to the objects.METHOD 
  # creates a new cart or returns the current cart stored in session
class CartManager(models.Manager):
    def new_cart_or_get(self, request):
        cart_id = request.session.get("cart_id", None)
        if request.user.is_authenticated:
          qs = self.get_queryset().filter(user=request.user)
          if qs.count() == 1:
              cart_obj = qs.first()
              new_obj = False
              request.session['cart_id'] = cart_obj.id
              return cart_obj, new_obj
            
        # if there is a cart id in session 
        qs = self.get_queryset().filter(id=cart_id)
        if qs.count() == 1:
            new_obj = False
            cart_obj = qs.first()
            if request.user.is_authenticated and cart_obj.user is None:
                  cart_obj.user = request.user
                  cart_obj.save()
            request.session['cart_id'] = cart_obj.id
            return cart_obj, new_obj
          
        # new cart created
        cart_obj = Cart.objects.new(user=request.user)
        new_obj = True
        request.session['cart_id'] = cart_obj.id    
        return cart_obj, new_obj

    def new(self, user=None):
        user_obj = None
        if user is not None:
            if user.is_authenticated:
                user_obj = user
        return self.model.objects.create(user=user_obj)



#  ------------------------ CART MODEL ---------------------------
class Cart(models.Model):
  user = models.OneToOneField(User, null=True, blank=True, on_delete=models.CASCADE)
  products = models.ManyToManyField(Product, blank=True)
  subtotal = models.DecimalField(decimal_places=2, max_digits=7, default=0.00)
  total = models.DecimalField(decimal_places=2, max_digits=7, default=0.00)
  
  updated = models.DateTimeField(auto_now=True)
  timestamp = models.DateTimeField(auto_now_add=True)
  
  objects = CartManager()
  



# check manyToMany Changes and update cart total
def m2m_cart_reciever(sender, instance, action, *args, **kwargs):
  if action == 'post_add' or action == 'post_remove' or action == 'post_clear':
    total = 0
    for product in instance.products.all():
      total += product.price
    print(total)    
    instance.subtotal = total
  instance.save()
m2m_changed.connect(m2m_cart_reciever, sender=Cart.products.through)

# update total when presave
def pre_save_cart(sender, instance, *args, **kwargs):
  if instance.subtotal > 0:
    instance.total = instance.subtotal + 10
  else:
    instance.total = 0.00
  
pre_save.connect(pre_save_cart, sender=Cart)