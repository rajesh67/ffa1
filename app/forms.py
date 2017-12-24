from django import forms

from app.models import PageQuestion, Volunteer
from django_summernote.widgets import SummernoteWidget, SummernoteInplaceWidget
from django.core.mail import send_mail

class QuestionForm(forms.ModelForm):
	class Meta:
		model=PageQuestion
		fields=('question', 'answer')
		widgets={
			'answer':SummernoteWidget(),
		}

class QuestionUpdateForm(forms.ModelForm):
	class Meta:
		model=PageQuestion
		fields=('answer',)
		widgets={
			'answer':SummernoteWidget(),
		}

class VolunteerSignupForm(forms.ModelForm):
	class Meta:
		model = Volunteer
		fields = '__all__'
		widgets={

		}

	def send_mail(self):
		send_mail(
			"Volunteer Signup with Friends For Animal",
			"Thank You for showing your interest in us",
			"rajeshmeena.iitkgp@gmail.com",
			["samir.30chandu@gmail.com",],
			fail_silently=False,
		)