from django import forms
from django.contrib.auth.forms import UserCreationForm # Molde para o formulário
from django.contrib.auth.models import User # Tabela do banco de dados

class CreateUserForm(UserCreationForm):
   class Meta:
       model = User
       fields = ['username', 'email', 'password']