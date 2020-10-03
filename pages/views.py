from django.shortcuts import render,redirect
from .forms import ContactForm

def home_page(req):
  return render(req,'home_page.html',{})


def about_page(req):
  return render(req,'about_page.html',{})


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