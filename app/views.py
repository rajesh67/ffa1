# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, render_to_response
# Create your views here.
from app.forms import VolunteerSignupForm
from blogs.models import Article
from app.models import PageQuestion, Donor, Volunteer
from app.forms import QuestionForm, QuestionUpdateForm
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView
from django.views.generic.base import View, TemplateView
from django_summernote.widgets import SummernoteWidget, SummernoteInplaceWidget

def index(request):
	return render(request, 'home.html', {'object_list': Article.objects.all()})

def about_us(request):
	return render(request, 'page.html',{'title':"About FFA", "questions":PageQuestion.objects.filter(category__name=4)})

def events(request):
	return render(request, 'programs.html', {'title':"Our Programs"})
def thank_you(request):
	return render(request, 'page.html', {'thank_you':'Thank You Very much for showing interest in us', "title":"Request For Membeship/Volunteer"})

def volunteer_thanks(request):
	return render(request, 'thanks.html',{})

def contact_us(request):
	return render(request, 'page.html',{'title':"Contact us / Reach FFA", "questions":PageQuestion.objects.filter(category__name=5)})

class VolunteerCreateView(CreateView):
	model=Volunteer
	template_name='page.html'
	success_url='/thank-you/#content'
	fields='__all__'


	def get_context_data(self, *args, **kwargs):
		context=super(VolunteerCreateView, self).get_context_data(*args, **kwargs)
		context['title']="Request to become an active ffa member"

class VolunteerView(CreateView):
	template_name="volunteer.html"
	form_class=VolunteerSignupForm
	success_url='/thanks/'

	def form_valid(self, form):
		# form.send_mail()
		return super(VolunteerView, self).form_valid(form)

class AboutUSView(TemplateView):
	template_name="about_us.html"

	def get_context_data(self, *args, **kwargs):
		context=super(AboutUSView, self).get_context_data(*args, **kwargs)
		context['questions']=PageQuestion.objects.filter(category__name=4)
		return context

class MedicationView(TemplateView):
	template_name="page.html"

	def get_context_data(self, *args, **kwargs):
		context=super(MedicationView, self).get_context_data(*args, **kwargs)
		context['questions']=PageQuestion.objects.filter(category__name=1)
		context['title']='Pet/Stray Animal Medication'
		return context

class AdoptionView(TemplateView):
	template_name="page.html"

	def get_context_data(self, *args, **kwargs):
		context=super(AdoptionView, self).get_context_data(*args, **kwargs)
		context['questions']=PageQuestion.objects.filter(category__name=2)
		context['title']='Pet Adoption and Care'
		return context

class DonationView(TemplateView):
	template_name="page.html"

	def get_context_data(self, *args, **kwargs):
		context=super(DonationView, self).get_context_data(*args, **kwargs)
		context['questions']=PageQuestion.objects.filter(category__name=3)
		context['title']='Donate to Support this Cause'
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
	template_name="page.html"

	def get_context_data(self, *args, **kwargs):
		context=super(DonorListView, self).get_context_data(*args, **kwargs)
		context['donors']=Donor.objects.all()
		context['title']='People Who Supports FFA'
		return context