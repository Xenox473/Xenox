from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from .logic import *
from .models import album

# Create your views here.

def homepage(request):
    album_list = album.objects.all()
    artist_list = artist.objects.all()
    for item in album_list:
        item.delete()
    for item in artist_list:
        item.delete()
    return render(request, 'spotify_app/homepage.html')

def albums(request):
    findalbums()
    findnewalbums()
    findrecentlyplayed()
    gettopartists()
    personal_album_list = album.objects.filter(type = 'personal')
    new_album_list = album.objects.filter(type = 'new')
    recent_list = album.objects.filter(type = 'recent')
    topartist = artist.objects.filter(type = 'top')
    print(personal_album_list)
    context = {
        'personal': personal_album_list,
        'new': new_album_list,
        'recent' : recent_list,
        'top' : topartist
    }
    return render(request, 'spotify_app/albums.html', context)

def albuminfo(request, image_id):
    albuminfo = getalbuminfo(image_id)
    artist = getartistid(albuminfo)
    related_artist = getrelatedartists(artist)
    track_list = gettracks(albuminfo)
    context = {
        'album': albuminfo,
        'related_artist' : related_artist,
        'track_list': track_list
    }
    return render(request, 'spotify_app/albuminfo.html', context)

def artistinfo(request, artist_id):
    artistinfo = artist.objects.get(id=artist_id)
    related_artist = getrelatedartists(artistinfo.identifier)
    albums = getartistalbums(artistinfo)
    context = {
        'artist' : artistinfo,
        'related_artist' : related_artist,
        'albums': albums
    }
    return render(request, 'spotify_app/artist.html', context)
