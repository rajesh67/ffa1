# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import *
from django.urls import reverse
# Create your models here.

class Article(models.Model):
<<<<<<< HEAD
	title=models.CharField(max_length=500)
	subtitle=models.CharField(max_length=250)
	cover_image=models.ImageField(upload_to='uploads/blogs/', default="/media/images/fbook.png")
	background_image=models.ImageField(upload_to='uploads/blogs/', default="/media/images/fbook.png")
=======
	title=models.CharField(max_length=250)
	subtitle=models.CharField(max_length=250,default="nothing")
	image=models.ImageField(upload_to='uploads/blogs', default="image.png")
>>>>>>> 670b2cc7d6e065f2900e993257efb4190b38894b
	text=models.TextField()
	pub_date=models.DateTimeField()
	user=models.ForeignKey(User, on_delete=models.CASCADE)

	def __str__(self):
		return self.title

	def get_absolute_url(self):
		return reverse('article-detail', kwargs={'pk':self.pk})
		