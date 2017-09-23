# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-09-23 15:13
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('QA_blog', '0037_auto_20170917_1723'),
    ]

    operations = [
        migrations.CreateModel(
            name='HighestRated',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('highr_image', models.ImageField(blank=True, null=True, upload_to='images')),
                ('highr_title', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='TopFiveGames',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('topfive_image', models.ImageField(blank=True, null=True, upload_to='images')),
                ('topfive_title', models.CharField(max_length=200)),
            ],
        ),
    ]
