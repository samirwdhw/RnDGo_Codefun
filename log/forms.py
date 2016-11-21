from django.contrib.auth.forms import AuthenticationForm 
from django import forms
from django.contrib.auth.models import User
from django.forms import ModelForm

class LoginForm(AuthenticationForm):
    username = forms.CharField(label="Username", max_length=30, 
                               widget=forms.TextInput(attrs={'class': 'form-control', 'name': 'username'}))
    password = forms.CharField(label="Password", max_length=30, 
                               widget=forms.PasswordInput(attrs={'class': 'form-control', 'name': 'password'}))

class UserForm(ModelForm):
	
	username = forms.CharField(label="Username", max_length=30, 
                               widget=forms.TextInput(attrs={'class': 'form-control', 'name': 'username'}))
	email = forms.CharField(label="Email", max_length=30, 
                               widget=forms.TextInput(attrs={'class': 'form-control', 'name': 'email'}))
	password = forms.CharField(label="Password", max_length=30, 
                               widget=forms.PasswordInput(attrs={'class': 'form-control', 'name': 'password'}))

	class Meta:
		password = forms.CharField(widget=forms.PasswordInput())
		model = User
		fields = ('username', 'email', 'password')

