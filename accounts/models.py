from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

class UserManager(BaseUserManager):
  def create_user(self, email, password=None, is_active=True, is_admin=False):
    if not email:
      raise ValueError('User must have an email')
    if not password:
      raise ValueError('User must have a password')
    new_user = self.model(
      email = self.normalize_email(email)
    )
    new_user.set_password(password)
    new_user.active = is_active
    new_user.admin = is_admin
    new_user.save(using=self._db)
    return new_user
  
  def create_superuser(self, email, password=None):
    new_superuser = self.create_user(
      email,
      password = password,
      is_admin=True
    )
    

# Create your models here.
class User(AbstractBaseUser):
  email = models.EmailField(max_length=255, unique=True)
  full_name = models.CharField(max_length=100, blank=True, null=True)
  active = models.BooleanField(default=True)
  admin = models.BooleanField(default=False)
  
  objects = UserManager()
  
  USERNAME_FIELD = 'email'
  REQUIRED_FIELDS = []
  
  def __str__(self):
    return self.full_name
  
