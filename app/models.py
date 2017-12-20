# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

CAT_CHOICES=(
	('1', 'Medication/Sponse'),
	('2', 'Adoption'),
	('3', 'Donation'),
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

class Donor(models.Model):
	name=models.CharField(max_length=100)
	email=models.CharField(max_length=250)
	amount=models.PositiveIntegerField(default=111)

	def __str__(self):
		return self.name