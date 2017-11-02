# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-29 07:23
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fruit', '0009_auto_20171029_1335'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='video',
            options={'verbose_name': '\u679c\u56ed\u89c6\u9891', 'verbose_name_plural': '\u679c\u56ed\u89c6\u9891'},
        ),
        migrations.AlterField(
            model_name='video',
            name='content',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='video',
            name='video',
            field=models.FileField(null=True, upload_to='static/media'),
        ),
    ]
