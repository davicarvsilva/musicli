from django.urls import path, include


from . import views


app_name = 'users'

urlpatterns = [
    path('register/', views.userRegister, name="register"),
    path('login/', views.userLogin, name="login"),
    path('logout/', views.userLogout, name="logout"),
    path('user_profile/', views.userProfile, name="user_profile"),
]
