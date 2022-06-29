from django.urls import path, include

from . import views

app_name = 'users'

urlpatterns = [
    path('logout/', views.userLogout, name="logout"),
    path('profile/', views.userProfile, name="user_profile"),
]
