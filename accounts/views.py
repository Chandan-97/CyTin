from django.shortcuts import render, redirect, HttpResponse

from django.contrib.auth import *
from .form import LoginForm, RegisterForm, RequestnewForm
from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.template.loader import render_to_string
from .tokens import account_activation_token

import sendgrid
import os
from sendgrid.helpers.mail import *


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

def requestnew_view(request):
	user = request.user

	if(user.is_authenticated() == False):
		return redirect("/login")

	form = RequestnewForm(request.POST or None)

	if form.is_valid():
		Software = form.save(commit=False)
		Software.software = form.cleaned_data.get("Software")
		if(form.cleaned_data.get("Version")):
			Software.version = form.cleaned_data.get("Version")
		if(form.cleaned_data.get("Comment")):
			Software.comment = form.cleaned_data.get("Comment")
		Software.save()
	return render(request, "requestnew_form.html", {"form" : form})

def register_view(request):
	print(request.user.is_authenticated())
	form = RegisterForm(request.POST or None)

	if form.is_valid():
		user = form.save(commit=False)
		password = form.cleaned_data.get("password")
		user.set_password(password)
		user.is_active = False
		user.save()
		current_site = get_current_site(request)

		sg = sendgrid.SendGridAPIClient(apikey=os.environ.get('SENDGRID_API_KEY'))
		from_email = Email("iamoneofmykind@gmail.com")
		to_email = Email(form.cleaned_data.get("email"))
		subject = "Activate your CyTin account"
		content = Content("text/plain", account_activation_token.make_token(user))
		mail = Mail(from_email, subject, to_email, content)
		response = sg.client.mail.send.post(request_body=mail.get())
		return HttpResponse('Please confirm your email address to complete the registration')
	else:
		form = RegisterForm()
	return render(request, "login_form.html", {"form":form})

	# 	new_user = authenticate(username=user.username, password=user.password)
	# 	login(request, user)
	# 	print(request.user.is_authenticated())
	# 	return redirect("/")
	# return render(request, "login_form.html", {"form" : form})

def activate(request, uidb64, token):
	try:
		uid = force_text(urlsafe_base64_decode(uidb64))
		user = User.objects.get(pk=uid)
	except(TypeError, ValueError, OverflowError, User.DoesNotExist):
		user = None

	if user is not None and account_activation_token.check_token(user, token):
		user.is_active = True
		user.save()
		login(request, user)
		return HttpResponse('Thank you for your email confirmation. Now you can login your account.')
	else:
	    return HttpResponse('Activation link is invalid!')