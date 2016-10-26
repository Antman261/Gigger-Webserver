# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from __future__ import unicode_literals
from djorm_pgfulltext.models import SearchManager
from djorm_pgfulltext.fields import VectorField
from django.db import models
# from pg_fts.fields import TSVectorField

class FacebookElement(models.Model):
    fb_id = models.BigIntegerField(unique=True, db_index=True)

    class Meta:
        abstract = True

class Agent(FacebookElement):
    username = models.CharField(unique=True, max_length=255, db_index=True)
    name = models.CharField(max_length=255)

    class Meta:
        abstract = True


class Location(models.Model):
    location_id = models.BigAutoField(primary_key=True)
    city = models.CharField(max_length=45, blank=True, db_index=True)
    country = models.CharField(max_length=45, blank=True, db_index=True)
    latitude = models.FloatField(null=True)
    longitude = models.FloatField(null=True)
    state = models.CharField(max_length=45, blank=True, db_index=True)
    street = models.CharField(max_length=45, blank=True)
    zip = models.CharField(max_length=45, blank=True)
    added = models.DateTimeField(blank=True, null=True, auto_now_add=True)


class Account(models.Model):
    account_id = models.AutoField(primary_key=True)
    email_address = models.CharField(max_length=255)
    session_token = models.CharField(max_length=255, blank=True)
    first_name = models.CharField(max_length=255, blank=True)
    last_name = models.CharField(max_length=255, blank=True)
    fb_id = models.BigIntegerField(unique=True, null=True)
    fb_longlived_token = models.CharField(max_length=500, blank=True)
    gender = models.CharField(max_length=255, blank=True)
    locale = models.CharField(max_length=255, blank=True)
    timezone = models.CharField(max_length=255, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    last_login = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return self.first_name +" "+self.last_name


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
    accounts = models.ManyToManyField(Account)

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


class Event(FacebookElement):
    event_id = models.AutoField(primary_key=True)
    venue = models.ForeignKey(Venue, models.DO_NOTHING)
    name = models.CharField(max_length=255, blank=True)
    description = models.TextField(blank=True)
    cover_source = models.CharField(max_length=500, blank=True)
    start_time = models.CharField(max_length=30, blank=True)
    timezone = models.CharField(max_length=45, blank=True)
    updated_time = models.DateTimeField(blank=True, null=True)
    ticket_uri = models.CharField(max_length=255, blank=True)
    event_type = models.CharField(max_length=50)
    created = models.DateTimeField(auto_now_add=True)
    edited = models.DateTimeField(blank=True, null=True, auto_now=True)
    deleted = models.BooleanField(default=0)

    def __str__(self):
        return self.name


class Genre(models.Model):
    genre_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    meta_description = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return self.name


class Performer(Agent):
    performer_id = models.AutoField(primary_key=True)
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
    band_type = models.CharField(max_length=55)
    record_label = models.CharField(max_length=255, blank=True)
    talking_about_count = models.PositiveIntegerField(null=True)
    website = models.CharField(max_length=255, blank=True)
    twitter_handle = models.CharField(max_length=255, blank=True)
    sound_path = models.URLField(max_length=500, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    edited = models.DateTimeField(blank=True, null=True, auto_now=True)
    email_address = models.EmailField(max_length=255, blank=True)
    deleted = models.BooleanField(default=0)
    # Foreign
    location = models.ForeignKey(Location, models.DO_NOTHING, blank=True, null=True)
    events = models.ManyToManyField(Event)
    genres = models.ManyToManyField(Genre, through="PerformerGenre")
    accounts = models.ManyToManyField(Account)

    #Fulltextindex
    genre_index = VectorField()
    objects = SearchManager(
        fields = (('about', 'A'), ('bio', 'B'), ('genre', 'A'), ('description', 'B')),
        config = 'pg_catalog.english', # this is default
        search_field = 'genre_index', # this is default
        auto_update_search_field = True
    )
    # fts_index = TSVectorField(
    #     (('about', 'A'), ('bio', 'B'), ('genre', 'A'), ('description', 'B')),
    #     dictionary='english'
    # )

    def __str__(self):
        return self.name


class PerformerCrawlMeta(models.Model):
    performer_crawl_meta = models.OneToOneField(Performer, models.DO_NOTHING, primary_key=True)
    num_crawls = models.IntegerField(null=True)
    band_likes_page = models.IntegerField(null=True)
    venue_likes_page = models.IntegerField(null=True)
    num_references = models.IntegerField(null=True)
    last_crawl_timestamp = models.DateTimeField(blank=True, null=True)


class PerformerGenre(models.Model):
    performer = models.ForeignKey(Performer, models.DO_NOTHING)
    genre = models.ForeignKey(Genre, models.DO_NOTHING, db_index=True)
    genre_score = models.FloatField()

    class Meta:
        unique_together = (('performer', 'genre'),)


class PerformerSearchLog(models.Model):
    search_id = models.BigAutoField(primary_key=True)
    account = models.ForeignKey(Account, models.DO_NOTHING, null=True)
    genre = models.CharField(max_length=100, blank=True) ## Not a key because genre can be -1 or 'any', which don't map to genres in the model but represent any genre
    has_sound = models.CharField(max_length=50, blank=True)
    band_type = models.CharField(max_length=100, blank=True)
    country = models.CharField(max_length=255, blank=True)
    state = models.CharField(max_length=255, blank=True)
    city = models.CharField(max_length=255, blank=True)
    min_likes = models.IntegerField(null=True)
    max_likes = models.CharField(max_length=100, blank=True)
    page = models.IntegerField(null=True)
    set_size = models.IntegerField(null=True)
    origin = models.CharField(max_length=255, blank=True)
    search_timestamp = models.DateTimeField(auto_now_add=True)



###
#   Dead classes: These tables may still exist in the db and might be reused in the future, but for now they are irrelevant
###
#
#
# class EventWorksheet(models.Model):
#     event = models.OneToOneField(Event, models.DO_NOTHING, primary_key=True)
#     load_in = models.TextField(blank=True)
#     sound_check = models.TextField(blank=True)
#     payment_details = models.TextField(blank=True)
#     mixer = models.TextField(blank=True)
#     band_gear = models.TextField(blank=True)
#     rider = models.TextField(blank=True)
#     door_spots = models.TextField(blank=True)
#     promo_publicity = models.TextField(blank=True)
#     venue_trading_times = models.TextField(blank=True)
#     staging = models.TextField(blank=True)
#     volume_management = models.TextField(blank=True)
#     created = models.DateTimeField(auto_now_add=True)
#
# class VenueWorksheet(models.Model):
#     venue = models.OneToOneField(Venue, models.DO_NOTHING, primary_key=True)
#     load_in = models.TextField(blank=True)
#     sound_check = models.TextField(blank=True)
#     payment_details = models.TextField(blank=True)
#     mixer = models.TextField(blank=True)
#     band_gear = models.TextField(blank=True)
#     rider = models.TextField(blank=True)
#     door_spots = models.TextField(blank=True)
#     promo_publicity = models.TextField(blank=True)
#     venue_trading_times = models.TextField(blank=True)
#     staging = models.TextField(blank=True)
#     volume_management = models.TextField(blank=True)
#     created = models.DateTimeField(auto_now_add=True)
#
#
# class Promoter(models.Model):
#     promoter_id = models.AutoField(db_column='PromoterID', primary_key=True)
#     account_id = models.ForeignKey('Account', models.DO_NOTHING, db_column='PromoterAccountID')
#     first_name = models.CharField(db_column='PromoterFirstName', max_length=255)
#     last_name = models.CharField(db_column='PromoterLastName', max_length=255)
#     email_address = models.CharField(db_column='PromoterEmailAddress', max_length=55, blank=True, null=True)
#     phone_number = models.CharField(db_column='PromoterPhoneNumber', max_length=55, blank=True, null=True)
#     organisation = models.CharField(db_column='PromoterOrganisation', max_length=100, blank=True, null=True)
#     created_datetime = models.DateTimeField(db_column='PromoterCreatedDateTime')
#     edited_datetime = models.DateTimeField(db_column='PromoterEditedDateTime', blank=True, null=True)
# #    events = models.ManyToManyField(Event, models.DO_NOTHING, through="PromoterEvents")
#
#     class Meta:
#         managed = False
#         db_table = 'Promoter'
#
#
# class PromoterEvents(models.Model):
#     promoter_id = models.ForeignKey(Promoter, models.DO_NOTHING, db_column='PromoterID')
#     event_id = models.ForeignKey(Event, models.DO_NOTHING, db_column='EventID')
#
#     class Meta:
#         managed = False
#         db_table = 'PromoterEvents'
#         unique_together = (('promoter_id', 'event_id'),)
#
#
# class Countries(models.Model):
#     country_code = models.CharField(db_column='countryCode', max_length=2)
#     country_name = models.CharField(db_column='countryName', max_length=45)
#     north = models.CharField(max_length=30, blank=True, null=True)
#     south = models.CharField(max_length=30, blank=True, null=True)
#     east = models.CharField(max_length=30, blank=True, null=True)
#     west = models.CharField(max_length=30, blank=True, null=True)
#     continent_name = models.CharField(db_column='continentName', max_length=15, blank=True, null=True)
#     continent = models.CharField(max_length=2, blank=True, null=True)
#     iso_alpha3 = models.CharField(db_column='isoAlpha3', max_length=3, blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'countries'
#
# class PerformerEvent(models.Model):
#     performer_id = models.ForeignKey(Performer, models.DO_NOTHING, db_column="PerformerID")
#     event_id = models.ForeignKey(Event, models.DO_NOTHING, db_column="EventID")
#
#     class Meta:
#         managed = False
#         db_table = 'PerformerEvent'
#         unique_together = (('performer_id', 'event_id'),)
#
# class PendingAdmin(models.Model):
#     pending_admin_id = models.AutoField(db_column='PendingAdminID', primary_key=True)
#     code = models.CharField(max_length=255)
#     class_field = models.CharField(db_column='class', max_length=255)  # Field renamed because it was a Python reserved word.
#     id = models.IntegerField(db_column='ID')
#     email = models.CharField(max_length=255, blank=True)
#     used = models.IntegerField()
#     created_datetime = models.DateTimeField(db_column='CreatedDateTime', auto_now_add=True)
#
#     class Meta:
#         managed = False
#         db_table = 'PendingAdmin'
#
# class Image(models.Model):
#     image_id = models.AutoField(db_column='ImageID', primary_key=True)
#     type_id = models.ForeignKey('ImageType', models.DO_NOTHING, db_column='ImageTypeID', blank=True, null=True)
#     url = models.CharField(db_column='ImageURL', max_length=255, blank=True, null=True)
#     alt_text = models.CharField(db_column='ImageAltText', max_length=255, blank=True, null=True)
#     created_datetime = models.DateTimeField(db_column='ImageCreatedDateTime')
#
#     class Meta:
#         managed = False
#         db_table = 'Image'
#
#
# class ImageType(models.Model):
#     image_type_id = models.IntegerField(db_column='ImageTypeID', primary_key=True)
#     type_extension = models.CharField(db_column='ImageTypeExtension', max_length=255, blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'ImageType'
#
# class PerformerReferral(models.Model):
#     referring_performer_id = models.IntegerField(db_column='ReferringPerformerID')
#     invited_performer_id = models.IntegerField(db_column='InvitedPerformerID')
#     claimed = models.IntegerField(db_column='Claimed')
#     created_timestamp = models.DateTimeField(db_column='CreatedTimestamp')
#     claimed_timestamp = models.DateTimeField(db_column='ClaimedTimestamp', blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'PerformerReferral'
#         unique_together = (('referringperformerid', 'invitedperformerid'),)
#
# class Set(models.Model):
#     set_id = models.AutoField(db_column='SetID', primary_key=True)
#     event_id = models.ForeignKey(Event, models.DO_NOTHING, db_column='EventID')
#     performer_id = models.ForeignKey(Performer, models.DO_NOTHING, db_column='PerformerID', blank=True, null=True)
#     set_number = models.SmallIntegerField(db_column='SetNumber', blank=True, null=True)
#     start_time = models.CharField(db_column='SetStartTime', max_length=30, blank=True, null=True)
#     end_time = models.CharField(db_column='SetEndTime', max_length=30, blank=True, null=True)
#     stage_number = models.IntegerField(db_column='StageNumber', blank=True, null=True)
#     stage_nickname = models.CharField(db_column='StageNickName', max_length=255, blank=True, null=True)
#     created_datetime = models.DateTimeField(db_column='SetCreatedDateTime')
#     edited_datetime = models.DateTimeField(db_column='SetEditedDateTime', blank=True, null=True)
#     deleted = models.IntegerField(db_column='SetDeleted')
#
#     class Meta:
#         managed = False
#         db_table = 'Set'
#
# class ServiceCategory(models.Model):
#     service_category_id = models.AutoField(db_column='ServiceCategoryID', primary_key=True)
#     name = models.CharField(db_column='Name', max_length=255, blank=True, null=True)
#     description = models.TextField(db_column='Description', blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'Serv_iceCategory'
#
#
# class ServiceProvider(models.Model):
#     service_provider_id = models.BigAutoField(db_column='ServiceProviderID', primary_key=True)
#     fb_id = models.BigIntegerField(db_column='FB_ID')
#     name = models.CharField(max_length=255)
#     description = models.TextField()
#     discount_percentage = models.IntegerField()
#     discount_code = models.CharField(max_length=255, blank=True, null=True)
#     username = models.CharField(max_length=255, blank=True, null=True)
#     website = models.CharField(max_length=255, blank=True, null=True)
#     country = models.CharField(max_length=255)
#     state = models.CharField(max_length=255, blank=True, null=True)
#     city = models.CharField(max_length=255, blank=True, null=True)
#     likes = models.IntegerField()
#     created = models.DateTimeField(db_column='ServiceProviderCreated', blank=True, null=True)
#     edited = models.DateTimeField(db_column='ServiceProviderEdited', blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'ServiceProvider'
#
#     def __str__(self):
#         return self.name
#
#
# class ServiceProviderAccount(models.Model):
#     account_id = models.IntegerField(db_column='AccountID')
#     service_provider_id = models.BigIntegerField(db_column='ServiceProviderID')
#
#     class Meta:
#         managed = False
#         db_table = 'ServiceProviderAccount'
#         unique_together = (('serviceproviderid', 'accountid'),)
#
#
# class ServiceProviderCategory(models.Model):
#     service_category_id = models.IntegerField(db_column='ServiceCategoryID')
#     service_provider_id = models.BigIntegerField(db_column='ServiceProviderID')
#
#     class Meta:
#         managed = False
#         db_table = 'ServiceProviderCategory'
#         unique_together = (('servicecategoryid', 'serviceproviderid'),)
#
#
# class ServiceProviderClickLog(models.Model):
#     service_provider_id = models.BigIntegerField(db_column='ServiceProviderID')
#     account_id = models.IntegerField(db_column='AccountID')
#     location = models.CharField(db_column='Location', max_length=255)
#     datetime = models.DateTimeField(db_column='DateTime')
#
#     class Meta:
#         managed = False
#         db_table = 'ServiceProviderClickLog'
#
#
# class ServiceProviderPrice(models.Model):
#     service_provider_priceid = models.BigAutoField(db_column='ServiceProviderPriceID', primary_key=True)
#     service_provider_id = models.BigIntegerField(db_column='ServiceProviderID', blank=True, null=True)
#     price = models.IntegerField(db_column='Price', blank=True, null=True)
#     description = models.CharField(db_column='Description', max_length=255, blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'ServiceProviderPrice'
#
#
# class ServiceProviderReview(models.Model):
#     service_provider_review_id = models.BigAutoField(db_column='ServiceProviderReviewID', primary_key=True)
#     service_provider_id = models.BigIntegerField(db_column='ServiceProviderID')
#     reviewer_account_id = models.IntegerField(db_column='ReviewerAccountID')
#     content = models.TextField(db_column='Content', blank=True, null=True)
#     rating = models.SmallIntegerField(db_column='Rating')
#     score = models.IntegerField(db_column='Score')
#     deleted = models.IntegerField(db_column='Deleted', blank=True, null=True)
#     flag_count = models.IntegerField(db_column='FlagCount', blank=True, null=True)
#     created = models.DateTimeField(db_column='ReviewCreated')
#     edited = models.DateTimeField(db_column='ReviewEdited')
#
#     class Meta:
#         managed = False
#         db_table = 'ServiceProviderReview'
