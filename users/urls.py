from django.urls import path, include

from . import views

app_name = 'users'

urlpatterns = [
    path('logout/', views.userLogout, name="logout"),
    path('profile/', views.userProfile, name="user_profile"),

    # override the SignupView of django-allauth
    path("accounts/signup/", views.account_signup_view, name="signup"),
    # this is the default config for django-allauth
    path("accounts/", include("allauth.urls")),

]
