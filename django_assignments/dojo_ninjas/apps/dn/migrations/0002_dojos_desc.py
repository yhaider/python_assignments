# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-07-19 19:18
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dn', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='dojos',
            name='desc',
            field=models.CharField(default='these dojos were made prior to desc', max_length=255),
            preserve_default=False,
        ),
    ]
