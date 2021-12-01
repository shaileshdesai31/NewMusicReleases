import spotipy
#from spotipy.oauth2 import SpotifyClientCredentials -- this line is in case Spotify credentials are used

#Basic cover art grabber using the "album_id" of a song

track_id = 'ADD_ID'
spotify = spotipy.Spotify()
track = spotify.album(track_id)
print(track['images'][0]['url'])