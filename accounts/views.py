from django.shortcuts import render

from django.contrib.auth import *
from .form import LoginForm


# Create your views here.

def login_view(request):
	form = LoginForm(request.POST or None)

	# Getting Values from form
	if form.is_valid():
		username = form.cleaned_data.get("username")
		password = form.cleaned_data.get("password")
		# print(username)
		# print(password)

	# Send it to render into page "login_form.html"
	return render(request, "login_form.html", {"form" : form})

def logout_view(request):
	return render(request, "logout_form.html", {})

def register_view(request):
	return render(request, "register_form.html", {})