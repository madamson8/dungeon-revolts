# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-02-26 00:58
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0008_itemtype_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='character',
            name='sin_level',
            field=models.SmallIntegerField(blank=True, default=0, null=True),
        ),
    ]
