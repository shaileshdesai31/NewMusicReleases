import spotipy
#from spotipy.oauth2 import SpotifyClientCredentials -- this line is in case Spotify credentials are used

#Intro to seeing lastest releases of an artist

artist_id = 'ADD ID'
artist_uri = f'spotify:artist:{artist_id}'
spotify = spotipy.Spotify(requests_timeout=40)
results = spotify.artist_albums(artist_uri, album_type='album', limit=3) #can change 'album' to 'single'
albums = results['items']
for album in albums:
    print(f"{album['name']} ({album['release_date']}): https://open.spotify.com/album/{album['id']}")
