# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-12-06 17:48
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0024_auto_20171206_1740'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='genre',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='blog.Genre'),
        ),
    ]
