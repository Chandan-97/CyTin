from django.shortcuts import render, redirect

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
		return redirect("/")
	# Send it to render into page "login_form.html"
	return render(request, "login_form.html", {"form" : form})

def logout_view(request):
	logout(request)
	print(request.user.is_authenticated())
	return render(request, "login_form.html", {})

def register_view(request):
	print(request.user.is_authenticated())
	form = RegisterForm(request.POST or None)

	if form.is_valid():
		user = form.save(commit=False)
		password = form.cleaned_data.get("password")
		user.set_password(password)
		user.save()
		new_user = authenticate(username=user.username, password=user.password)
		login(request, user)
		print(request.user.is_authenticated())
		return redirect("/")
	return render(request, "login_form.html", {"form" : form})

	# 12:09