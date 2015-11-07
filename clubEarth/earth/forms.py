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
	password1 = forms.CharField(label="Password", required=True,
		widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password'}))
	password2 = forms.CharField(label="Confirm_Password", required=True,
		widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Confirm Password'}))
	email = forms.EmailField(label='Email', required=True, 
		widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email'}))

	class Meta:
		model = User
		fields= ["username", "password1", "password2", "email"]

class ThreadForm(forms.ModelForm):
	title = forms.CharField(label="Title", required=True, 
		widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Title', }))
	content = forms.CharField(label="Content", required=True,
		widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Content', }))

	class Meta:
		model = Thread
		fields = ["title", "content"]

class CommentForm(forms.ModelForm):
	content = forms.CharField(label="Content", required=True,
		widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Comment', }))

	class Meta:
		model = Comment
		fields = ["content"]

class EventForm(forms.ModelForm):
	name = forms.CharField(label="Event Name", required=True,
		widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Event Name'}))
	description = forms.CharField(label="Description", required=True, 
		widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Description'}))
	location1 = forms.CharField(label="location1", required=True,
		widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Address 1'}))
	location2 = forms.CharField(label ="location2", required=True, 
		widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Address 2'}))

	class Meta:
		model = Event
		fields = ["name", "description", "location1", "location2"]

