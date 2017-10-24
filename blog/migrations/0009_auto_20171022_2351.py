# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-10-22 23:51
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0008_post_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, null=True)),
            ],
        ),
        migrations.AlterField(
            model_name='post',
            name='ABV',
            field=models.CharField(default='comming soon', max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='Cocktails',
            field=models.TextField(default='comming soon', null=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='Distillery',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AlterField(
            model_name='post',
            name='Estimated_price',
            field=models.CharField(default='comming soon', max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='Tasting_note',
            field=models.TextField(default='comming soon', null=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='flavor_text',
            field=models.TextField(default='comming soon'),
        ),
        migrations.AlterField(
            model_name='post',
            name='image',
            field=models.ImageField(blank=True, default='settings.MEDIA_ROOT/document/404.png', upload_to='document/'),
        ),
        migrations.AlterField(
            model_name='post',
            name='url',
            field=models.URLField(blank=True, null=True),
        ),
    ]
