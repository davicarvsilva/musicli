from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required


from .forms import CreateUserForm

@login_required(login_url='account_login')
def userLogout(request):
   logout(request)
   return redirect('account_login')

@login_required(login_url='account_login')
def userProfile(request):
    return render(request, "users/user_profile.html")


