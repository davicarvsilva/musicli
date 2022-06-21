from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from .forms import CreateUserForm


def userRegister(request):
    if request.user.is_authenticated:
        return redirect('core:index')

    form = CreateUserForm()

    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('core:index')

    return render(request, 'users/user_register.html', {'form':form})

def userLogin(request):
   if request.user.is_authenticated:
       return redirect('core:index')

   if request.method == 'POST':
       username = request.POST.get('username')
       password = request.POST.get('password')

       user = authenticate(request, username=username, password=password)

       if user is not None:
           login(request, user)
           return redirect('core:index')
       else:
           messages.info(request, 'Usuário ou senha incorretos')

   return render(request, 'users/user_login.html')

@login_required(login_url='users:login')
def userLogout(request):
   logout(request)
   return redirect('users:login')

@login_required(login_url='users:login')
def userProfile(request):
    return render(request, "users/user_profile.html")


