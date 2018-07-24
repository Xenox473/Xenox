from django.db import models

# Create your models here.

class Image(models.Model):
    description = models.CharField(max_length= 25, blank=True, null=True, default = 0)
    image_url = models.CharField(max_length= 50, blank=True, null=True, default = 0)

class BlogPost(models.Model):
    title = models.CharField(max_length= 25, blank=True, null=True, default = 0)
    subtitle = models.CharField(max_length= 25, blank=True, null=True, default = 0)
    body = models.CharField(max_length= 10000, blank=True, null=True, default = 0)
    image =  models.ForeignKey(Image,on_delete=models.CASCADE)
