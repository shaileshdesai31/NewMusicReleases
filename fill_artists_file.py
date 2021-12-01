import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

# This script fills ARTISTS_FILE_NAME file with the artists in all the songs of PLAYLIST_ID
# Format:
#Artist_Name: artist_id
#Artist_Name: artist_id
# ...

ARTISTS_FILE_NAME = "artists.txt"
PLAYLIST_ID = 'ADD ID'
CLIENT_ID = "xxx"
CLIENT_SECRET = "xxx"  # Obtain client_id and client_secret from creating an app on a Spotify for Developers account


def read_current_artists() -> set:
    with open(ARTISTS_FILE_NAME) as file:
        artists = set()
        for line in file:
            artists.add(line.rstrip())
    return artists


def add_artists(songs: list, current_artists) -> None:
    with open(ARTISTS_FILE_NAME, 'a') as file:
        for song in songs:
            artists = []
            for artist in song['track']['artists']:
                artists.append(f"{artist['name']}: {artist['id']}")
            for artist in artists:
                if artist not in current_artists:
                    current_artists.add(artist)
                    file.write(artist + '\n')


if __name__ == '__main__':
    spotify = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials(
        client_id=CLIENT_ID,
        client_secret=CLIENT_SECRET,
        requests_timeout=100))
    playlist = spotify.playlist(PLAYLIST_ID)
    current_artists = read_current_artists()
    add_artists(playlist['tracks']['items'], current_artists)
