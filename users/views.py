from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from allauth.account.views import SignupView

from .forms import UserCreateForm

from allauth.account.views import SignupView


class AccountSignupView(SignupView):
    template_name = "users/signup.html"
    form_class = UserCreateForm

    def get(self, request, *args, **kwargs):
        form = self.form_class()
        return render(request, self.template_name, {'form': form})

    # You can also override some other methods of SignupView
    # Like below:
    # def form_valid(self, form):
    #     ...
    #
    # def get_context_data(self, **kwargs):
    #     ...

account_signup_view = AccountSignupView.as_view()



@login_required(login_url='account_login')
def userLogout(request):
   logout(request)
   return redirect('account_login')

@login_required(login_url='account_login')
def userProfile(request):
    return render(request, "users/user_profile.html")


