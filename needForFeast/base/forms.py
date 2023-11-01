from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import *


class CustomerSignupForm(UserCreationForm):
    email = forms.EmailField(max_length=200, help_text='Required')

    class Meta:
        model = Customer
        fields = ('username','name', 'email', 'password1', 'password2','phonenumbers','addresses')  

class OwnerSignupForm(UserCreationForm):
    email = forms.EmailField(max_length=200, help_text='Required')

    class Meta:
        model = Owner
        fields = ('username','name', 'email', 'password1', 'password2','phonenumbers','addresses')  

class DelivererSignupForm(UserCreationForm):
    email = forms.EmailField(max_length=200, help_text='Required')

    class Meta:
        model = Deliverer
        fields = ('username','name', 'email', 'password1', 'password2','phonenumbers','addresses')  