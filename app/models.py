# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.


class AdoptionPageQuestion(models.Model):
	question=models.CharField(max_length=250)
	answer=models.TextField(max_length=10000)

	def __str__(self):
		return self.question