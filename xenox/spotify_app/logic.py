from .models import album, artist, track
import sys
import spotipy
import spotipy.util as util

def findalbums():
    scope = 'user-library-read user-read-recently-played user-top-read'
    username = 'oblixy@yahoo.com'
    token = util.prompt_for_user_token(username, scope,client_id = '1fbf3e9edded4216bc9f91e6f9e6acf0', client_secret = '8257d880c0124789a40a16a3fc101257',redirect_uri='http://localhost:8000/spotify')
    if token:
        sp = spotipy.Spotify(auth=token)
        results = sp.current_user_saved_albums(offset = 20)
        for item in results['items']:
            track = item['album']
            try:
                (album.objects.get(name = track['name']))
            except:
                tempAlbum = album(name = track['name'], artist = track['artists'][0]['name'], image = track['images'][0]['url'], releaseDate = track['release_date'], identifier = track['id'], type = 'personal')
                tempAlbum.save()
    else:
        print ("Can't get token for", username)
    return

def findnewalbums():
    scope = 'user-library-read user-read-recently-played user-top-read'
    username = 'oblixy@yahoo.com'
    token = util.prompt_for_user_token(username, scope,client_id = '1fbf3e9edded4216bc9f91e6f9e6acf0', client_secret = '8257d880c0124789a40a16a3fc101257',redirect_uri='http://localhost:8000/spotify')
    if token:
        sp = spotipy.Spotify(auth=token)
        results = sp.new_releases(limit = 50)
        for item in results['albums']['items']:
            # print (item['name'] + ' - ' + item['artists'][0]['name'])
            try:
                (album.objects.get(name = item['name']))
            except:
                tempAlbum = album(name = item['name'], artist = item['artists'][0]['name'], image = item['images'][0]['url'], releaseDate = item['release_date'], identifier = item['id'], type = 'new')
                tempAlbum.save()
    else:
        print ("Can't get token for", username)
    return

def findrecentlyplayed():
    scope = 'user-library-read user-read-recently-played user-top-read'
    username = 'oblixy@yahoo.com'
    token = util.prompt_for_user_token(username, scope,client_id = '1fbf3e9edded4216bc9f91e6f9e6acf0', client_secret = '8257d880c0124789a40a16a3fc101257',redirect_uri='http://localhost:8000/spotify')
    if token:
        sp = spotipy.Spotify(auth=token)
        results = sp.current_user_recently_played(limit = 50)
        for item in results['items']:
            # print (item['name'] + ' - ' + item['artists'][0]['name'])
            try:
                (album.objects.get(name = item['track']['album']['name']))
            except:
                result = sp.album(item['track']['album']['id'])
                tempAlbum = album(name = result['name'], artist = result['artists'][0]['name'], image = result['images'][0]['url'], identifier = result['id'], releaseDate = result['release_date'], type = 'recent')
                tempAlbum.save()
    else:
        print ("Can't get token for", username)
    return

def gettopartists():
    scope = 'user-library-read user-read-recently-played user-top-read'
    username = 'oblixy@yahoo.com'
    token = util.prompt_for_user_token(username, scope,client_id = '1fbf3e9edded4216bc9f91e6f9e6acf0', client_secret = '8257d880c0124789a40a16a3fc101257',redirect_uri='http://localhost:8000/spotify')
    if token:
        sp = spotipy.Spotify(auth=token)
        results = sp.current_user_top_artists(limit=50)
        for item in results['items']:
            try:
                (artist.objects.get(name = item['name']))
            except:
                tempArtist = artist(name = item['name'], image = item['images'][0]['url'], identifier = item['id'], type = 'top')
                tempArtist.save()
    else:
        print ("Can't get token for", username)
    return

def getalbuminfo(image_id):
    albuminfo = album.objects.get(id = image_id)
    return albuminfo

def getartistid(albuminfo):
    scope = 'user-library-read user-read-recently-played user-top-read'
    username = 'oblixy@yahoo.com'
    token = util.prompt_for_user_token(username, scope,client_id = '1fbf3e9edded4216bc9f91e6f9e6acf0', client_secret = '8257d880c0124789a40a16a3fc101257',redirect_uri='http://localhost:8000/spotify')
    result = []
    if token:
        sp = spotipy.Spotify(auth=token)
        result = sp.album(albuminfo.identifier)
    return result['artists'][0]['id']

def getrelatedartists(artist_id):
    scope = 'user-library-read user-read-recently-played user-top-read'
    username = 'oblixy@yahoo.com'
    token = util.prompt_for_user_token(username, scope,client_id = '1fbf3e9edded4216bc9f91e6f9e6acf0', client_secret = '8257d880c0124789a40a16a3fc101257',redirect_uri='http://localhost:8000/spotify')
    result = []
    if token:
        sp = spotipy.Spotify(auth=token)
        results = sp.artist_related_artists(artist_id)
        for item in results['artists']:
            try:
                tempArtist = (artist.objects.get(name = item['name']))
            except:
                tempArtist = artist(name = item['name'], image = item['images'][0]['url'], identifier = item['id'], type = 'related')
                tempArtist.save()
            finally:
                result.append(tempArtist)
    else:
        print ("Can't get token for", username)
    return result

def gettracks(album):
    scope = 'user-library-read user-read-recently-played user-top-read'
    username = 'oblixy@yahoo.com'
    token = util.prompt_for_user_token(username, scope,client_id = '1fbf3e9edded4216bc9f91e6f9e6acf0', client_secret = '8257d880c0124789a40a16a3fc101257',redirect_uri='http://localhost:8000/spotify')
    result = []
    if token:
        sp = spotipy.Spotify(auth=token)
        results = sp.album_tracks(album.identifier)
        # pp.pprint(results)
        for item in results['items']:
            try:
                tempTrack = (track.objects.get(name = item['name']))
            except:
                tempTrack = track(name = item['name'], artist = item['artists'][0]['name'], album = album.name, track_number = item['track_number'], preview_url = item['preview_url'], duration_ms = item['duration_ms'])
                tempTrack.save()
            finally:
                result.append(tempTrack)
    else:
        print ("Can't get token for", username)
    return result

def getartistalbums(artist):
    scope = 'user-library-read user-read-recently-played user-top-read'
    username = 'oblixy@yahoo.com'
    token = util.prompt_for_user_token(username, scope,client_id = '1fbf3e9edded4216bc9f91e6f9e6acf0', client_secret = '8257d880c0124789a40a16a3fc101257',redirect_uri='http://localhost:8000/spotify')
    result = []
    if token:
        sp = spotipy.Spotify(auth=token)
        results = sp.artist_albums(artist.identifier)
        # pp.pprint(results)
        for item in results['items']:
            try:
                tempAlbum = (album.objects.get(name = item['name']))
            except:
                tempAlbum = album(name = item['name'], artist = item['artists'][0]['name'], image = item['images'][0]['url'], releaseDate = item['release_date'], identifier = item['id'], type = 'individuals')
                tempAlbum.save()
            finally:
                result.append(tempAlbum)
    else:
        print ("Can't get token for", username)
    return result
