# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desidered behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from __future__ import unicode_literals

from django.db import models


class Diary(models.Model):
    entry_no = models.AutoField(primary_key=True)
    userid = models.CharField(max_length=30)
    date = models.DateField(blank=True, null=True)
    office_or_home = models.CharField(max_length=50)
    data = models.TextField()

    class Meta:
        managed = False
        db_table = 'diary'


class JourneyDetails(models.Model):
    starting_point = models.CharField(max_length=20, blank=True, null=True)
    destination = models.CharField(max_length=20, blank=True, null=True)
    date = models.DateField(blank=True, null=True)
    time = models.TimeField(blank=True, null=True)
    journey_time = models.IntegerField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'journey_details'


class Tutorials(models.Model):
    category = models.CharField(max_length=50, blank=True, null=True)
    sub_category = models.CharField(max_length=50, blank=True, null=True)
    tags = models.TextField(blank=True, null=True)
    data = models.TextField(blank=True, null=True)
    date = models.DateTimeField(blank=True, null=True)
    image_path = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tutorials'
