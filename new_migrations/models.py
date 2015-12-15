# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desidered behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from __future__ import unicode_literals

from django.db import models


class TopicDetails(models.Model):
    topic = models.CharField(max_length=50)
    image = models.CharField(max_length=60)
    date = models.DateTimeField()
    privacy = models.CharField(max_length=15)
    details = models.TextField()
    handle = models.ForeignKey('UserInfo', models.DO_NOTHING, db_column='handle')

    class Meta:
        managed = False
        db_table = 'topic_details'


class UserInfo(models.Model):
    handle = models.CharField(primary_key=True, max_length=30)
    name = models.CharField(max_length=50)
    password = models.CharField(max_length=40)
    email = models.CharField(max_length=50)
    country = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'user_info'
