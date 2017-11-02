# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import *

# Register your models here.
class FruitAdmin(admin.ModelAdmin):
	list_display = ('title', 'content', 'id')
	search_fields = (['title'])

class VideoAdmin(admin.ModelAdmin):
	list_display = ('title',)
	search_fields = (['title'])

class ActiviyAdmin(admin.ModelAdmin):
	list_display = ('category', 'id')

admin.site.register(Fruit, FruitAdmin)
admin.site.register(Activity, ActiviyAdmin)
admin.site.register(Video, VideoAdmin)
admin.site.register(Document)