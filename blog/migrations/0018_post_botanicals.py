# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-11-14 19:03
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0017_botanicals'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='botanicals',
            field=models.ManyToManyField(blank=True, to='blog.Botanicals'),
        ),
    ]
