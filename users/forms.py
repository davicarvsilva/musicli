from django import forms
from django.contrib.auth.forms import UserCreationForm # Molde para o formulário
from django.contrib.auth.models import User # Tabela do banco de dados


class DateInput(forms.DateInput):
    input_type = 'date'

class UserCreateForm(UserCreationForm):
    birth_date = forms.DateField(required=True, widget=DateInput())

    class Meta:
        model = User
        fields = ("username", "email", "birth_date", "password1", "password2")

    def __init__(self, *args, **kwargs):
        super(UserCreateForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs['placeholder'] = "Username"
        self.fields['email'].widget.attrs['placeholder'] = "Email"
        self.fields['password1'].widget.attrs['placeholder'] = "Password"
        self.fields['password2'].widget.attrs['placeholder'] = "Confirm password"

    def save(self, commit=True):
        user = super(UserCreateForm, self).save(commit=False)
        user.birth_date = self.cleaned_data["birth_date"]
        if commit:
            user.save()
        return user