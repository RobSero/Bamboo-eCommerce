from django.db import models
from django.conf import settings
from products.models import Product
from django.db.models.signals import m2m_changed, pre_save

User = settings.AUTH_USER_MODEL

#  add new methods to the objects.METHOD 
class CartManager(models.Manager):
  # creates a new cart or returns the current cart stored in session
  def new_cart_or_get(self, req):
    # check cart_id in session
      cart_id = req.session.get("cart_id", None)
      query = self.get_queryset().filter(id=cart_id)
      # check if a cart is returned
      if query.count() == 1:
        new_cart = False
        cart = query.first()
        if req.user.is_authenticated and cart.user is None:
            cart.user = req.user
            cart.save()
      else:
        # create cart if one does not exist in session
            cart = Cart.objects.new(user=req.user)
            new_cart = True
            req.session['cart_id'] = cart.id
      return cart, new_cart
    
  #  create new cart, pass user from session, set to None if does not exist
  def new(self, user=None):
    user_object = None
    if user is not None:
      if user.is_authenticated:
        user_object = user
    return self.model.objects.create(user=user_object)



#  ------------------------ CART MODEL ---------------------------
class Cart(models.Model):
  user = models.ForeignKey(User, null=True, blank=True, on_delete=models.PROTECT)
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