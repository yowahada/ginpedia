# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-11-21 14:30
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0018_post_botanicals'),
    ]

    operations = [
        migrations.AddField(
            model_name='botanicals',
            name='thumnail',
            field=models.ImageField(blank=True, null=True, upload_to='botanical'),
        ),
    ]
