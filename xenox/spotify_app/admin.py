from django.contrib import admin
from .models import album, artist, track

# Register your models here.
admin.site.register(album)
admin.site.register(artist)
admin.site.register(track)
