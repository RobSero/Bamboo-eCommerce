from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

class UserManager(BaseUserManager):
  def create_user(self,  email, password=None, is_active=True, is_admin=False, is_staff=False, full_name=None):
    if not email:
      raise ValueError('User must have an email')
    if not password:
      raise ValueError('User must have a password')
    new_user = self.model(
      email = self.normalize_email(email)
    )
    new_user.set_password(password)
    new_user.full_name = full_name
    new_user.active = is_active
    new_user.admin = is_admin
    new_user.staff = is_staff
    new_user.save(using=self._db)
    return new_user
  
  def create_superuser(self, email, password=None):
    new_superuser = self.create_user(
      email,
      password = password,
      is_admin=True,
      is_staff=True
    )
    

# Create your models here.
class User(AbstractBaseUser):
  email = models.EmailField(max_length=255, unique=True)
  full_name = models.CharField(max_length=100, blank=True, null=True)
  active = models.BooleanField(default=True)
  admin = models.BooleanField(default=False)
  staff = models.BooleanField(default=False)
  
  objects = UserManager()
  
  USERNAME_FIELD = 'email'
  REQUIRED_FIELDS = []
  
  def __str__(self):
    return self.email
  
  def is_staff(self):
    return self.staff
  
  def is_admin(self):
      return self.admin
    
  def has_perm(self,perm, obj=None):
    return True
  
  def has_module_perms(self, app_label):
    return True
