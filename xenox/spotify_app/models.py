from django.db import models

# Create your models here.
class album(models.Model):
    name= models.CharField(max_length= 25, blank=True, null=True, default = 0)
    artist = models.CharField(max_length= 25, blank=True, null=True, default = 0)
    image = models.CharField(max_length= 50, blank=True, null=True, default = 0)
    releaseDate = models.CharField(max_length= 25, blank=True, null=True, default = 0)
    identifier = models.CharField(max_length= 25, blank=True, null=True, default = 0)
    type = models.CharField(max_length= 25, blank=True, null=True, default = 0)

class artist(models.Model):
    name= models.CharField(max_length= 25, blank=True, null=True, default = 0)
    image = models.CharField(max_length= 50, blank=True, null=True, default = 0)
    identifier = models.CharField(max_length= 25, blank=True, null=True, default = 0)
    type = models.CharField(max_length= 25, blank=True, null=True, default = 0)

class track(models.Model):
    name = models.CharField(max_length= 25, blank=True, null=True, default = 0)
    artist = models.CharField(max_length= 25, blank=True, null=True, default = 0)
    album = models.CharField(max_length= 25, blank=True, null=True, default = 0)
    track_number = models.CharField(max_length= 25, blank=True, null=True, default = 0)
    preview_url = models.CharField(max_length= 25, blank=True, null=True, default = 0)
    duration_ms = models.IntegerField()
