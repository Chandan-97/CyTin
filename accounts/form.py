from django.contrib.auth import (authenticate, 
								login, 
								logout,
								get_user_model)
from django import forms

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



class RegisterForm(forms.Form):
	name = forms.CharField()
	email = forms.CharField()
	username = forms.CharField()
	password = forms.CharField(widget=forms.PasswordInput)
	retype_password = forms.CharField(widget=forms.PasswordInput)
