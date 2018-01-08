from django import forms

GENDER_CHOICES=(
	('M', 'Male'),
	('F', 'Female'),
	('O', 'Others'),
)

class VolunteerSignupForm(forms.Form):
	name = forms.CharField(max_length=100)
	email= forms.CharField(max_length=10)
	# profession = forms.IntegerField(default=0)
	# contact = forms.IntegerField(defult=10) 
	# alternate = forms.IntegerField(default=0)
	# gender = forms.DateTimeField(add_now=True)
	# age = forms.CharField(max_length=100)
	# location = forms.CharField(max_length=100)
	# nation = forms.CharField(max_length=100)
	# how_did_you_hear_about_us = forms.CharField(max_length=100)
	# why_do_you_want_to_volunteer = forms.CharField(max_length=100)
