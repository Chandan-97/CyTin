from django.shortcuts import render

from django.contrib.auth import *
from .form import LoginForm, RegisterForm


# Create your views here.

def login_view(request):
	form = LoginForm(request.POST or None)

	# Getting Values from form and validation
	if form.is_valid():	# clean() from forms.py is called
		username = form.cleaned_data.get("username")
		password = form.cleaned_data.get("password")
		# print(username)
		# print(password)

		#user is available
		user = authenticate(username=username, password=password)
		login(request, user)
		print (request.user.is_authenticated())

	# Send it to render into page "login_form.html"
	return render(request, "login_form.html", {"form" : form})

def logout_view(request):
	logout(request)
	print(request.user.is_authenticated())
	return render(request, "login_form.html", {})

def register_view(request):
	form = RegisterForm(request.POST or None)

	if form.is_valid():
		name 	= form.cleaned_data.get("name")
		username= form.cleaned_data.get("username")
		email 	= form.cleaned_data.get("email")
		password= form.cleaned_data.get("password")
		retype_password = form.cleaned_data.get("retype_password")
	return render(request, "register_form.html", {"form" : form})