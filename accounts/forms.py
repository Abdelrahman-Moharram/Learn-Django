from django.contrib.auth.forms import UserCreationForm
from django import forms
from .models import account,employeer,employee
from django.conf import settings

class userForm(UserCreationForm):
    class Meta:
        model   = account
        fields  = '__all__'
        exclude = ('slug','joined_at','is_admin','is_staff','is_superuser','last_login','password','user_type')

class employeerForm(forms.ModelForm):
    class Meta:
        model   = employeer
        fields  = ["linkedin"]


class employeeForm(forms.ModelForm):
    class Meta:
        model   =   employee
        fields  =   '__all__'
        exclude = ("user",)
