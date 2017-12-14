# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.views.generic.dates import ArchiveIndexView, DayArchiveView, DateDetailView
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
# Create your views here.
from blogs.models import Article
from django.utils import timezone

class DaywiseArchiveView(DayArchiveView):
	queryset=Article.objects.all()
	date_field='pub_date'
	make_object_list=True

class ArticleListView(ListView):
	template_name='blogs/article_archive.html'
	model = Article

	def get_context_data(self, **kwargs):
		context=super(ArticleListView, self).get_context_data(**kwargs)
		context['now']=timezone.now()
		return context


class ArticleDetailView(DetailView):
	template_name = 'blogs/article_detail.html'
	model=Article

	def get_context_data(self, **kwargs):
		context=super(ArticleDetailView, self).get_context_data(**kwargs)
		context['now']=timezone.now()
		return context