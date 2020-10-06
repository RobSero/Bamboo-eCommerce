from django.shortcuts import render, redirect
from .forms import LoginForm, RegisterForm
from django.contrib.auth import authenticate, login, get_user_model
from django.utils.http import is_safe_url


#  --------------- LOGIN FORM --------------------

def login_page(req):
  login_form = LoginForm(req.POST or None)
  print(req.user.is_authenticated)
  next_ = req.GET.get('next')
  next_post = req.POST.get('next')
  redirect_path = next_ or next_post or None
  # validate form
  if login_form.is_valid():
    # check if user is valid
    username = req.POST.get('username')
    password = req.POST.get('password')
    user = authenticate(req, username=username, password=password)
    if user is not None:
      # success - login user and redirect
      login(req,user)
      if is_safe_url(redirect_path,req.get_host()):
        return redirect(redirect_path)
      else:
        return redirect('home')
    else:
      print('WRONG CREDENTIALS')
    
  context = {
    'form' : login_form
  }
  return render(req,'auth/login.html',context)


#  --------------- REGISTER FORM --------------------

User = get_user_model()
def register_page(req):
  new_email = req.POST.get('email', None)
  register_form = RegisterForm(req.POST or None)
  if register_form.is_valid():
    username = register_form.cleaned_data.get('username')
    email = register_form.cleaned_data.get('email')
    password = register_form.cleaned_data.get('password')
    new_user = User.objects.create_user(username,email,password)
    print(new_user)
    return redirect('login')
  register_form = RegisterForm(initial={'email': req.POST.get('email')})
  context = {
    'form' : register_form
  }
  return render(req,'auth/register.html',context)

