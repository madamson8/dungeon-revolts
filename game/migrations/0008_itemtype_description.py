# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-02-26 00:51
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0007_merge'),
    ]

    operations = [
        migrations.AddField(
            model_name='itemtype',
            name='description',
            field=models.TextField(default='description'),
        ),
    ]
