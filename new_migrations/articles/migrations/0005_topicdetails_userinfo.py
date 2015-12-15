# -*- coding: utf-8 -*-
# Generated by Django 1.9c2 on 2015-12-13 20:11
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0004_auto_20151206_1928'),
    ]

    operations = [
        migrations.CreateModel(
            name='TopicDetails',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('topic', models.CharField(max_length=50)),
                ('image', models.CharField(max_length=60)),
                ('date', models.DateTimeField()),
                ('privacy', models.CharField(max_length=15)),
                ('details', models.TextField()),
            ],
            options={
                'db_table': 'topic_details',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='UserInfo',
            fields=[
                ('handle', models.CharField(max_length=30, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('password', models.CharField(max_length=40)),
                ('email', models.CharField(max_length=50)),
                ('country', models.CharField(max_length=20)),
            ],
            options={
                'db_table': 'user_info',
                'managed': False,
            },
        ),
    ]
