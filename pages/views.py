from django.shortcuts import render
from .forms import ContactForm, LoginForm

def home_page(req):
  return render(req,'home_page.html',{})

def about_page(req):
  return render(req,'about_page.html',{})

def login_page(req):
  return render(req,'auth/login.html',{})

def register_page(req):
  return render(req,'auth/register.html',{})




def contact_page(req):
  contact_form = ContactForm(req.POST or None)
  context = {
    'form': contact_form
  }
  if contact_form.is_valid():
    print(contact_form.cleaned_data)
  else:
    print('wrong')
  return render(req,'contact/view.html',context)