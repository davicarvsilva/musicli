from django.urls import path, include


from . import views


app_name = 'userss'

urlpatterns = [
    path('register/', views.userRegister, name="register"),
    path('login/', views.userLogin, name="login"),
    path('logout/', views.userLogout, name="logout"),
    path('profile/', views.userProfile, name="user_profile"),
]
