from django.shortcuts import render

def home_page(req):
  return render(req,'home_page.html',{})

def about_page(req):
  return render(req,'about_page.html',{})

def contact_page(req):
  return render(req,'contact_page.html',{})