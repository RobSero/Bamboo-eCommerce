from django import forms
from django.contrib.auth import get_user_model

User = get_user_model()


class LoginForm(forms.Form):
  username = forms.CharField(widget=forms.TextInput(attrs={
    'class': 'form-input form-style-override', 
    'placeholder': 'Message'
    }), label='')
  password = forms.CharField(widget=forms.PasswordInput(attrs={
    'class': 'form-input form-style-override', 
    'placeholder': 'Password'
    }), label='')
  
  
  
  
  
class RegisterForm(forms.Form):
  username = forms.CharField(widget=forms.TextInput(attrs={
    'class': 'form-input form-style-override', 
    'placeholder': 'Username'
    }), label='')
  email = forms.EmailField(widget=forms.EmailInput(attrs={
    'class': 'form-input form-style-override', 
    'placeholder': 'Email'
    }), label='')
  password = forms.CharField(widget=forms.PasswordInput(attrs={
    'class': 'form-input form-style-override', 
    'placeholder': 'Password'
    }), label='')
  password2 = forms.CharField(widget=forms.PasswordInput(attrs={
    'class': 'form-input form-style-override', 
    'placeholder': 'Confirm Password'
    }), label='')
  
  
  def clean_username(self):
    username = self.cleaned_data.get('username')
    find_users = User.objects.filter(username=username)
    if find_users.exists():
      raise forms.ValidationError('username already exists')
    return username
  
  
  def clean_email(self):
    email = self.cleaned_data.get('email')
    find_users = User.objects.filter(email=email)
    if find_users.exists():
      raise forms.ValidationError('email already exists')
    return email
    
    
  def clean(self):
    data = self.cleaned_data
    password = self.cleaned_data.get('password')
    password2 = self.cleaned_data.get('password2')
    if password != password2:
      raise forms.ValidationError('passwords do not match')
    return data