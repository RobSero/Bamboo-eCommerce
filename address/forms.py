from django import forms
from .models import Address


class AddressForm(forms.ModelForm):
  class Meta:
    model = Address
    fields = '__all__'
    exclude = ['user']
    
    widgets = {
  'address_name': forms.TextInput(attrs={
    'class': 'form-input form-style-override address-input', 
    'placeholder': 'Address No. / Name'
  }),
  'address_one': forms.TextInput(attrs={
    'class': 'form-input form-style-override address-input', 
    'placeholder': 'Address Line 1'
  }),
  'address_two': forms.TextInput(attrs={
    'class': 'form-input form-style-override address-input', 
    'placeholder': 'Address Line 2'
  }),
  'county': forms.TextInput(attrs={
    'class': 'form-input form-style-override address-input', 
    'placeholder': 'County'
  }),
  'postcode': forms.TextInput(attrs={
    'class': 'form-input form-style-override address-input', 
    'placeholder': 'Postcode'
  }),
        }




# class AddressForm(forms.ModelForm):
#   address_name = forms.CharField(widget=forms.TextInput(attrs={
#     'class': 'form-input form-style-override', 
#     'placeholder': 'Address No. / Name'
#   }), label='')
#   address_one = forms.CharField(widget=forms.TextInput(attrs={
#     'class': 'form-input form-style-override', 
#     'placeholder': 'Address Line One'
#   }), label='')
#   address_two = forms.CharField(widget=forms.TextInput(attrs={
#     'class': 'form-input form-style-override', 
#     'placeholder': 'Address Line Two'
#   }), label='')
#   county = forms.CharField(widget=forms.TextInput(attrs={
#     'class': 'form-input form-style-override', 
#     'placeholder': 'county'
#   }), label='')
#   postcode = forms.CharField(widget=forms.TextInput(attrs={
#     'class': 'form-input form-style-override', 
#     'placeholder': 'Postcode'
#   }), label='')
  
  
  