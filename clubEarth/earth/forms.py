from django import forms
from .models import *
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class ProfileForm(forms.ModelForm):

	class Meta:
		model = Profile
		exclude = ('user', )

class UserForm(UserCreationForm):
	username = forms.CharField(label="Username", required=True, 
		widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Username', }))
	email = forms.EmailField(label='Email', required=True, 
		widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email'}))

	class Meta:
		model = User
		fields= ["username", "password1", "password2", "email"]