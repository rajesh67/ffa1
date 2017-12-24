from django import forms

from app.models import PageQuestion, Volunteer
from django_summernote.widgets import SummernoteWidget, SummernoteInplaceWidget


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