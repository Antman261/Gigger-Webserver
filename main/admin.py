from django.contrib import admin
from .models import Performer, Event, Venue, Location, Genre

# Register your models here.
admin.site.register(Performer)
admin.site.register(Event)
admin.site.register(Venue)
admin.site.register(Location)
admin.site.register(Genre)
