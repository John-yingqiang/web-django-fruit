# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-19 03:57
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('fruit', '0002_auto_20171018_2223'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='article',
            name='image_detail',
        ),
    ]
