# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import *

# Create your models here.

class Article(models.Model):
	title=models.CharField(max_length=250)
	text=models.TextField()
	pub_date=models.DateTimeField()
	user=models.ForeignKey(User, on_delete=models.CASCADE)

	def __str__(self):
		return self.title
		