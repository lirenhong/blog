# -*- coding: utf-8 -*-
# Generated by Django 1.11.12 on 2018-04-17 12:41
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog_lrh', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Categpry',
            new_name='Category',
        ),
    ]
