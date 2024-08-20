

from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User, Profile


class UserRegisterForm(UserCreationForm):
	'''
		these fields take arguments (required=true/false).
		by default, required=true
	'''
	### add fields to this form
	email = forms.EmailField()
	usable_password = None

	class Meta:
		model = User
		fields = ["email", "password1", "password2", ] # "username" not in use


# after adding these forms, add it to the views.py
class UserUpdateForm(forms.ModelForm):
	'''
		these fields take arguments (required=true/false).
		by default, required=true
	'''
	email = forms.EmailField()

	class Meta:
		model = User
		fields = ["email"]	# add other attrs as needed

class ProfileUpdateForm(forms.ModelForm):
	class Meta:
		model = Profile 	# the model that is going to be affected by this form
		fields = ["alias", "image", "location", "quote", "about_me",]

		'''
			I removed these fields because they're also removed/commented-out from the Profile model.
			Uncomment them from the model, modify as needed, run migrations and then add them to the fields attribute of this form...if you want to.
		'''
		# "google", "linkedin", "github", "facebook", "twitter", "instagram", "school", "course", "year_in_school",
		# "user_group" field was not included for it will determine ranks in the future
		# "reach_me_intro", "profile_snippet" were not included due to redunduncy // just used "about_me" in its place on home_unauthed/home_unauthed.html
