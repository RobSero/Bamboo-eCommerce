from django import forms

class ContactForm(forms.Form):
  fullname = forms.CharField(widget=forms.TextInput(attrs={
    'class': 'form-input form-style-override', 
    'placeholder': 'Your full name',
    }), label='')
  email = forms.EmailField(widget=forms.TextInput(attrs={
    'class': 'form-input form-style-override', 
    'placeholder': 'Email'
    }), label='')
  content = forms.CharField(widget=forms.TextInput(attrs={
    'class': 'form-input form-style-override', 
    'placeholder': 'Message'
    }), label='')
  
  def clean_email(self):
    email = self.cleaned_data.get('email')
    if not '.com' in email:
      raise forms.ValidationError('valid email address is required')
    return email
  