from django.shortcuts import render,redirect
from .forms import ContactForm, LoginForm, RegisterForm
from django.contrib.auth import authenticate, login, get_user_model

def home_page(req):
  return render(req,'home_page.html',{})




def about_page(req):
  return render(req,'about_page.html',{})



#  --------------- LOGIN FORM --------------------

def login_page(req):
  login_form = LoginForm(req.POST or None)
  print(req.user.is_authenticated)
  # validate form
  if login_form.is_valid():
    # check if user is valid
    username = req.POST.get('username')
    password = req.POST.get('password')
    user = authenticate(req, username=username, password=password)
    if user is not None:
      # success - login user and redirect
      login(req,user)
      print(req.user.is_authenticated)
      return redirect('/login')
    else:
      print('WRONG CREDENTIALS')
    
  context = {
    'form' : login_form
  }
  return render(req,'auth/login.html',context)


#  --------------- REGISTER FORM --------------------

User = get_user_model()
def register_page(req):
  register_form = RegisterForm(req.POST or None)
  if register_form.is_valid():
    username = register_form.cleaned_data.get('username')
    email = register_form.cleaned_data.get('email')
    password = register_form.cleaned_data.get('password')
    new_user = User.objects.create_user(username,email,password)
    print(new_user)
    
    
  context = {
    'form' : register_form
  }
  return render(req,'auth/register.html',context)






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