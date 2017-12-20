# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, render_to_response
# Create your views here.
from app.froms import VolunteerSignupForm
from blogs.models import Article
from app.models import PageQuestion, Donor
from app.forms import QuestionForm, QuestionUpdateForm
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView
from django.views.generic.base import View, TemplateView
from django_summernote.widgets import SummernoteWidget, SummernoteInplaceWidget

def index(request):
	return render(request, 'home.html', {'object_list': Article.objects.all()})

def about_us(request):
	return render(request, 'about_us.html',{})

def events(request):
	return render(request, 'event.html', {})

def medication(request):
	return render(request, 'medication.html', {})

def volunteer(request):
	return render(request, 'volunteer.html', {'form':VolunteerSignupForm()})

def contact_us(request):
	return render(request, 'contact.html',{})

def adoptions(request):
	return render(request, 'adoption.html',{})

class MedicationView(TemplateView):
	template_name="medication.html"

	def get_context_data(self, *args, **kwargs):
		context=super(MedicationView, self).get_context_data(*args, **kwargs)
		context['questions']=PageQuestion.objects.filter(category__name=1)
		return context

class AdoptionView(TemplateView):
	template_name="adoption.html"

	def get_context_data(self, *args, **kwargs):
		context=super(AdoptionView, self).get_context_data(*args, **kwargs)
		context['questions']=PageQuestion.objects.filter(category__name=2)
		return context

class DonationView(TemplateView):
	template_name="donation.html"

	def get_context_data(self, *args, **kwargs):
		context=super(DonationView, self).get_context_data(*args, **kwargs)
		context['questions']=PageQuestion.objects.filter(category__name=3)
		return context

class AdoptionCreateView(CreateView):
	template_name="adoption_create.html"
	form_class=QuestionForm
	success_url="/"
	# fields=('question', 'answer')
	widgets={
		'answer':SummernoteWidget(),
	}

	def form_valid(self, form):
		return super(AdoptionCreateView, self).form_valid(form)

class AdoptionUpdateView(UpdateView):
	template_name="adoption_update.html"
	form_class=QuestionUpdateForm
	success_url='/'
	widgets={
		'answer':SummernoteWidget(),
	}

	def form_valid(self, *args, **kwargs):
		return super(AdoptionUpdateView, self).form_valid(*args, **kwargs)

class DonorListView(ListView):
	model=Donor
	template_name="donors_list.html"

	def get_context_data(self, *args, **kwargs):
		context=super(DonorListView, self).get_context_data(*args, **kwargs)
		return context