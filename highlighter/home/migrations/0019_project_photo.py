# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-11 12:56
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0018_remove_project_user_agent'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='photo',
            field=models.ImageField(blank=True, upload_to=''),
        ),
    ]
