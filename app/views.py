# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, render_to_response
# Create your views here.
from app.froms import VolunteerSignupForm
from blogs.models import Article

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

def donations(request):
	return render(request, 'donation.html',{})

def donors_list(request):
	return render(request, 'donors_list.html',{})