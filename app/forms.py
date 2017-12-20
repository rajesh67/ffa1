from django import forms

from app.models import AdoptionPageQuestion
from django_summernote.widgets import SummernoteWidget, SummernoteInplaceWidget


class AdoptionQuestionForm(forms.ModelForm):
	class Meta:
		model=AdoptionPageQuestion
		fields=('question', 'answer')
		widgets={
			'answer':SummernoteWidget(),
		}

class AdoptionQuestionUpdateForm(forms.ModelForm):
	class Meta:
		model=AdoptionPageQuestion
		fields=('answer',)
		widgets={
			'answer':SummernoteWidget(),
		}