# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2018-04-06 02:59
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CyTin_View', '0005_auto_20180314_0054'),
    ]

    operations = [
        migrations.CreateModel(
            name='Requestnew',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('software', models.CharField(max_length=30)),
                ('version', models.CharField(default='N/A', max_length=20, null=True)),
                ('comment', models.CharField(default='No Comments', max_length=600, null=True)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]