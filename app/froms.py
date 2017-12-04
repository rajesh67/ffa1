from django import forms

GENDER_CHOICES=(
	('M', 'Male'),
	('F', 'Female'),
	('O', 'Others'),
)

class VolunteerSignupForm(forms.Form):
	name = forms.CharField(max_length=100)
	gender = forms.CharField(max_length=10)
	age = forms.IntegerField()
	nationality = forms.CharField(max_length=30)
	date_of_birth = forms.DateTimeField()
	profession = forms.CharField(max_length=100)
	how_did_you_hear_about_us = forms.CharField(max_length=100)
	why_do_you_want_to_volunteer = forms.CharField(max_length=100)
