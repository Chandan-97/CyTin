from django.contrib.auth import (authenticate, 
								login, 
								logout,
								get_user_model)
from django import forms
from CyTin_View.models import Requestnew, Software

User = get_user_model()

# Add fields to the form
class LoginForm(forms.Form):
	username = forms.CharField()
	password = forms.CharField(widget=forms.PasswordInput)

	# if user not valid return him else continue
	def clean(self):
		cleaned_data = super(LoginForm, self).clean()
		username = cleaned_data.get("username")
		password = cleaned_data.get("password")

		user = authenticate(username=username, password=password)
		if not user:
			raise forms.ValidationError("User Doesnot Exist")

		# if not user.check_password(password):
		# 	raise forms.ValidationError("Incorrect Password")

		# if not user.is_active:
		# 	raise forms.ValidationError("User Inactive")
		# print("hello : " + user.__str__())
		return super(LoginForm, self).clean()

class RegisterForm(forms.ModelForm):
	# adding new field
	email2 = forms.EmailField(label="Confirm Email*")
	# overriting exeisting password field
	password = forms.CharField(widget=forms.PasswordInput)
	email = forms.EmailField(label="Email Address")
	# using field from user model, and using 
	# created fiels
	class Meta:
		model = User
		fields = [
			'username',
			'password',
			'email',
			'email2'
		]

	# if clean_password then we get data upto password field
	# to get upto email2 field clean_email2
	# order is important
	# we can use clean(self) also without worrying about order
	def clean_email2(self):
		cleaned_data = super(RegisterForm, self).clean()
		print(cleaned_data)
		email = cleaned_data.get("email")
		email2 = cleaned_data.get("email2")
		if email != email2:
			raise forms.ValidationError("Email must match")

		# email should be unique
		email_qs = User.objects.filter(email=email)
		if email_qs.exists():
			raise forms.ValidationError("This email is already Register")
		return email

class RequestnewForm(forms.ModelForm):
	Software = forms.CharField()
	Version  = forms.CharField()
	Comment  = forms.CharField(widget=forms.Textarea)

	class Meta:
		model = Requestnew
		fields = [
			'Software',
			'Version',
			'Comment',
		]

	def clean(self):
		cleaned_data = super(RequestnewForm, self).clean()
		print(cleaned_data)
		software = cleaned_data.get("Software")
		version  = cleaned_data.get("Version")

		print("Software : %s" %(software))
		print("version : %s" %(version))

		print("hello")
		requestnew_qs = Requestnew.objects.filter(software=software, version=version)
		print(requestnew_qs, cleaned_data)

		if(requestnew_qs.exists()):
			raise forms.ValidationError("Someone Else have already requested this software, we will upload it soon")
		software_qs = Software.objects.filter(title=software, version=version)
		print("world")
		print(software_qs, cleaned_data)
		if(software_qs.exists()):
			raise forms.ValidationError("Already been uploaded into the list, please check the website")
		return cleaned_data
