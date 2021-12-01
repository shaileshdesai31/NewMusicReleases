import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

# Intro to seeing lastest releases of an artist

CLIENT_ID = "xxx"
CLIENT_SECRET = "xxx"  # Obtain client_id and client_secret from creating an app on a Spotify for Developers account

artist_id = 'ADD ID'
artist_uri = f'spotify:artist:{artist_id}'
spotify = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials(
    client_id=CLIENT_ID,
    client_secret=CLIENT_SECRET,
    requests_timeout=100))
# Obtain client_id and client_secret from creating an app on a Spotify for Developers account
# requests_timeout can be changed depending on internet speed
# spotify credentials can be added into the parameters for the Spotify object

results = spotify.artist_albums(artist_uri, album_type='album', limit=3)  # can change 'album' to 'single'
albums = results['items']
for album in albums:
    print(f"{album['name']} ({album['release_date']}): https://open.spotify.com/album/{album['id']}")
