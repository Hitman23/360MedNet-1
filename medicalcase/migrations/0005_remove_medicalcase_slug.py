# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-06-02 13:49
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('medicalcase', '0004_auto_20170520_2140'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='medicalcase',
            name='slug',
        ),
    ]
