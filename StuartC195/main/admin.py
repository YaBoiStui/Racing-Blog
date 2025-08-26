from django.contrib import admin
from .models import RaceResult, Comment, Event

# Register your models here.
admin.site.register(RaceResult)
admin.site.register(Comment)
admin.site.register(Event)
