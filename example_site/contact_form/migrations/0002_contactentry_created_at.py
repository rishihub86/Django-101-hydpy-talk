# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-05-12 11:15
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('contact_form', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='contactentry',
            name='created_at',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]