# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-05-20 18:40
from __future__ import unicode_literals

import autoslug.fields
from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('medicalcase', '0003_auto_20170517_1930'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='medicalcase',
            options={'ordering': ['-created_at'], 'verbose_name_plural': 'Medical Cases'},
        ),
        migrations.AddField(
            model_name='medicalcase',
            name='slug',
            field=autoslug.fields.AutoSlugField(default=None, editable=False, null=True, populate_from='title', unique_with=('created_at',)),
        ),
        migrations.AddField(
            model_name='medicalcasecategory',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='medicalcasecategory',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='photo',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='photo',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
