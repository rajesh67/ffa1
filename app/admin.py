# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
# Register your models here.
from app.models import PageQuestion, Category, Donor, Volunteer

# Apply summernote to all TextField in model.
class AdoptionQuestionModelAdmin(SummernoteModelAdmin):  # instead of ModelAdmin
    summer_note_fields = '__all__'

admin.site.register(Category)
admin.site.register(Donor)
admin.site.register(Volunteer)
admin.site.register(PageQuestion, AdoptionQuestionModelAdmin)