# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-11-03 16:50
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0010_auto_20171025_1224'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='flavor_text',
            new_name='Botanical',
        ),
        migrations.RenameField(
            model_name='post',
            old_name='Cocktails',
            new_name='Flavor_text',
        ),
        migrations.AddField(
            model_name='post',
            name='Country',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='contact',
            name='contact_text',
            field=models.TextField(blank=True, max_length=300, verbose_name='内容'),
        ),
        migrations.AlterField(
            model_name='contact',
            name='mail',
            field=models.EmailField(blank=True, max_length=75, verbose_name='Mail'),
        ),
    ]
