from django import forms

class ContactForm(forms.Form):
  fullname = forms.CharField(widget=forms.TextInput(attrs={
    'class': 'form-input', 
    'placeholder': 'your full name'
    }))
  email = forms.EmailField()
  content = forms.CharField(widget=forms.Textarea())
  
  def clean_email(self):
    email = self.cleaned_data.get('email')
    if not '.com' in email:
      raise forms.ValidationError('valid email address is required')
    return email
  
  
class LoginForm(forms.Form):
  username = forms.CharField()
  password = forms.CharField(widget=forms.PasswordInput)