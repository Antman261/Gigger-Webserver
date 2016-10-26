# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from __future__ import unicode_literals
from django.db import models

import datetime

class FacebookElement(models.Model):
    fb_id = models.BigIntegerField(unique=True, db_index=True, db_column="FB_ID")

    class Meta:
        abstract = True

class Agent(FacebookElement):
    username = models.CharField(unique=True, max_length=255, db_index=True)
    name = models.CharField(max_length=255)

    class Meta:
        abstract = True


class Location(models.Model):
    location_id = models.BigAutoField(primary_key=True, db_column="LocationID")
    city = models.CharField(max_length=45, blank=True, db_index=True)
    country = models.CharField(max_length=45, blank=True, db_index=True)
    latitude = models.FloatField(null=True)
    longitude = models.FloatField(null=True)
    state = models.CharField(max_length=45, blank=True, db_index=True)
    street = models.CharField(max_length=45, blank=True)
    zip = models.CharField(max_length=45, blank=True)

    class Meta:
        managed = False
        db_table="tblLocation"


class Venue(Agent):
    venue_id = models.AutoField(primary_key=True)
    location = models.ForeignKey(Location, models.DO_NOTHING)
    capacity = models.IntegerField(blank=True)
    booking_contact = models.CharField(max_length=255, blank=True)
    about = models.CharField(max_length=255, blank=True)
    category = models.CharField(max_length=45, blank=True)
    checkins = models.IntegerField(null=True)
    cover_id = models.BigIntegerField(null=True)
    cover_source = models.CharField(max_length=500, blank=True)
    description = models.TextField(blank=True)
    likes = models.IntegerField(null=True)
    link = models.CharField(max_length=45, blank=True)
    phone = models.CharField(max_length=45, blank=True)
    talking_about_count = models.IntegerField(null=True)
    were_here_count = models.IntegerField(null=True)
    created = models.DateTimeField(blank=True, null=True, auto_now_add=True)
    edited = models.DateTimeField(auto_now=True)

    class Meta:
        managed = False

    def __str__(self):
        return self.name


class VenueTechSpec(models.Model):
    venue = models.OneToOneField(Venue, models.DO_NOTHING, primary_key=True)
    booking_contact = models.CharField(max_length=255, blank=True)
    production_contact = models.CharField(max_length=255, blank=True)
    venue_hire = models.TextField(blank=True)
    underage_band_members = models.TextField(blank=True)
    technical_info = models.TextField(blank=True)
    room_spec = models.TextField(blank=True)
    pa_spec = models.TextField(blank=True)
    extra_spec = models.TextField(blank=True)

    class Meta:
        managed = False


class Event(FacebookElement):
    event_id = models.AutoField(primary_key=True, db_column="EventID")
    # venue = models.ForeignKey(Venue, models.DO_NOTHING)
    name = models.CharField(max_length=255, blank=True)
    description = models.TextField(blank=True)
    cover_source = models.CharField(max_length=500, blank=True)
    start_time = models.CharField(max_length=30, blank=True)
    timezone = models.CharField(max_length=45, blank=True)
    updated_time = models.DateTimeField(blank=True, null=True)
    ticket_uri = models.CharField(max_length=255, blank=True)
    # event_type = models.CharField(max_length=50)
    # created = models.DateTimeField(auto_now_add=True)
    # edited = models.DateTimeField(blank=True, null=True, auto_now=True)
    # deleted = models.BooleanField(default=0)

    class Meta:
        managed = False
        db_table="tblEvent"

    def __str__(self):
        return self.name

    def reprJSON(self):
        d = dict()
        for a, v in self.__dict__.items():
            if hasattr(v, "reprJSON"):
                d[a] = v.reprJSON()
            elif isinstance(v, datetime.datetime):
                d[a] = v.strftime("%Y-%m-%d %H:%M:%S")
            elif type(v) is list and not isinstance(v, basestring):
                d[a] = []
                for obj in v:
                    if hasattr(obj, "reprJSON"):
                        obj = obj.reprJSON()
                    elif isinstance(v, datetime.datetime):
                        obj = obj.strftime("%Y-%m-%d %H:%M:%S")
                    d[a].append(obj)
            else:
                d[a] = v
        if "_state" in d:
            del d['_state']
        return d


class Genre(models.Model):
    genre_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    meta_description = models.CharField(max_length=255, blank=True)

    class Meta:
        managed = False

    def __str__(self):
        return self.name


class Performer(Agent):
    performer_id = models.AutoField(primary_key=True, db_column="PerformerID")
    about = models.CharField(max_length=255, blank=True)
    bio = models.TextField(blank=True)
    artists_we_like = models.CharField(max_length=255, blank=True)
    band_members = models.CharField(max_length=255, blank=True)
    booking_agent = models.CharField(max_length=255, blank=True)
    category = models.CharField(max_length=255, blank=True)
    cover_id = models.IntegerField(blank=True, null=True)
    cover_source = models.CharField(max_length=1000, blank=True)
    current_location = models.CharField(max_length=255, blank=True)
    description = models.TextField(blank=True)
    genre = models.CharField(max_length=255, blank=True)
    hometown = models.CharField(max_length=255, blank=True)
    likes = models.IntegerField(blank=True, null=True)
    link = models.CharField(max_length=255, blank=True)
    band_type = models.CharField(max_length=55, db_column="BandType")
    record_label = models.CharField(max_length=255, blank=True)
    talking_about_count = models.PositiveIntegerField(null=True)
    website = models.CharField(max_length=255, blank=True)
    twitter_handle = models.CharField(max_length=255, blank=True, db_column="PerformerTwitterHandle")
    sound_path = models.URLField(max_length=500, blank=True, db_column="PerformerSoundCloudPath")
    email_address = models.EmailField(max_length=255, blank=True, db_column="PerformerEmailAddress")
    deleted = models.BooleanField(default=0, db_column="Deleted")
    # Foreign
    location = models.ForeignKey(Location, models.DO_NOTHING, blank=True, null=True, db_column="LocationID")
    events = models.ManyToManyField(Event, through="PerformerEvent")

    class Meta:
        managed = False
        db_table="tblPerformer"

    def __str__(self):
        return self.name

class PerformerEvent(models.Model):
    performer_id = models.ForeignKey(Performer, models.DO_NOTHING, db_column="PerformerID")
    event_id = models.ForeignKey(Event, models.DO_NOTHING, db_column="EventID")

    class Meta:
        managed = False
        db_table="tblPerformerEvent"
        unique_together = (('performer_id', 'event_id'),)
