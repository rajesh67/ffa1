# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
# Register your models here.
from blogs.models import Article

# Apply summernote to all TextField in model.
class ArticleModelAdmin(SummernoteModelAdmin):  # instead of ModelAdmin
    summer_note_fields = '__all__'

admin.site.register(Article, ArticleModelAdmin)