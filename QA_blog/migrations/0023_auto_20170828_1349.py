# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-08-28 13:49
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('QA_blog', '0022_auto_20170828_1258'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='rating',
            field=models.IntegerField(choices=[(1, 'Awful'), (2, 'Poor'), (3, 'Average'), (4, 'Good'), (5, 'Outstanding')]),
        ),
    ]
