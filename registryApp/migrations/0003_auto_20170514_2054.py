# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-05-14 20:54
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('registryApp', '0002_auto_20170514_2052'),
    ]

    operations = [
        migrations.RenameField(
            model_name='system_services',
            old_name='image',
            new_name='image_path',
        ),
    ]
