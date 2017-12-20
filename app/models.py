# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

CAT_CHOICES=(
	('1', 'Adoption'),
	('2', 'Donation'),
	('3', 'Medication/Sponse'),
)

class Category(models.Model):
	name=models.CharField(max_length=1, choices=CAT_CHOICES, unique=True)

	def __str__(self):
		return self.name

class PageQuestion(models.Model):
	question=models.CharField(max_length=250)
	answer=models.TextField(max_length=10000)
	category=models.ForeignKey(Category, on_delete=models.CASCADE)

	def __str__(self):
		return self.question