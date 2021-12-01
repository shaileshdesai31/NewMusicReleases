import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

# Basic cover art grabber using the "album_id" of a song

CLIENT_ID = "xxx"
CLIENT_SECRET = "xxx"  # Obtain client_id and client_secret from creating an app on a Spotify for Developers account

track_id = 'ADD_ID'
spotify = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials(
    client_id=CLIENT_ID,
    client_secret=CLIENT_SECRET,
    requests_timeout=100))
track = spotify.album(track_id)
print(track['images'][0]['url'])
