from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.homepage),
    path('albums/', views.albums),
    path('albums/<int:image_id>', views.albuminfo),
    path('artist/<int:artist_id>', views.artistinfo)
]
