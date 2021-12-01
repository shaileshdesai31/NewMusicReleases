import spotipy
#from spotipy.oauth2 import SpotifyClientCredentials -- this line is in case Spotify credentials are used

#This script fills ARTISTS_FILE_NAME file with the artists in all the songs of PLAYLIST_ID
#Format:
#Artist_Name: artist_id
#Artist_Name: artist_id
# ...

ARTISTS_FILE_NAME = "artists.txt"
PLAYLIST_ID = '37i9dQZF1DX7Mq3mO5SSDc'


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
    spotify = spotipy.Spotify(requests_timeout=40)
    playlist = spotify.playlist(PLAYLIST_ID)
    current_artists = read_current_artists()
    add_artists(playlist['tracks']['items'], current_artists)
