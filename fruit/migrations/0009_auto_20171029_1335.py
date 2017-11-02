# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-29 05:35
from __future__ import unicode_literals

from django.db import migrations, models
import django_thumbs.db.models


class Migration(migrations.Migration):

    dependencies = [
        ('fruit', '0008_auto_20171027_1553'),
    ]

    operations = [
        migrations.AddField(
            model_name='fruit',
            name='detail',
            field=models.TextField(blank=True, verbose_name='\u4ea7\u54c1\u8be6\u60c5'),
        ),
        migrations.AlterField(
            model_name='fruit',
            name='content',
            field=models.TextField(verbose_name='\u7b80\u4ecb(\u5bf9\u6807\u9898\u7684\u7b80\u8ff0)'),
        ),
        migrations.AlterField(
            model_name='fruit',
            name='image_content1',
            field=django_thumbs.db.models.ImageWithThumbsField(blank=True, upload_to='static/images/app'),
        ),
        migrations.AlterField(
            model_name='fruit',
            name='image_content2',
            field=django_thumbs.db.models.ImageWithThumbsField(blank=True, upload_to='static/images/app'),
        ),
        migrations.AlterField(
            model_name='fruit',
            name='image_content3',
            field=django_thumbs.db.models.ImageWithThumbsField(blank=True, upload_to='static/images/app'),
        ),
    ]