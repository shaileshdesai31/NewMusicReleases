import datetime
import spotipy
import os
#from spotipy.oauth2 import SpotifyClientCredentials -- this line is in case Spotify credentials are used

# Have a file with Spotify artist ID's listed; format:
#Artist_Name: artist_id
ARTISTS_FILE_NAME = "artists.txt"
RELEASE_INTERVAL = 2  # All releases +- RELEASE_INTERVAL days from when executed will be reported


# Opens the the file of artists and returns a list of all the id's
def get_artists() -> ['']:
    with open(ARTISTS_FILE_NAME) as file:
        artist_ids = []
        for line in file:
            artist_ids.append(line[line.find(':') + 2:].rstrip())
    return artist_ids


# Given the Spotify object and an artist_id, the artist's last album
# and last three singles are checked to see if they meet the "new release"
# criteria. All "new releases" for the artist will be returned in a set.
# If there are no "new releases", an empty set will be returned.
def check_new_music(spotify: spotipy.Spotify, artist_id: str) -> set:
    artist_uri = f'spotify:artist:{artist_id}'
    albums = spotify.artist_albums(artist_uri, album_type='single', limit=3)['items']
    results_a = spotify.artist_albums(artist_uri, album_type='album', limit=1)['items']
    songs = set()
    for album in albums:
        if new_release(album['release_date']):
            songs.add(album['id'])
        else:
            break
    for album in results_a:
        if new_release(album['release_date']):
            songs.add(album['id'])
        else:
            break
    return songs


# Determines if a release is "new". We don't want to report old releases.
# If a release is within RELEASE_INTERVAL days from the date, it will be reported.
# Note a song/album could be released and have a future released date due to songs
# being available in certain regions.
def new_release(release_date_str: str) -> bool:
    try:
        release_date = datetime.date.fromisoformat(release_date_str)
    except ValueError:
        return False
    today = datetime.date.today()
    return today - datetime.timedelta(days=RELEASE_INTERVAL) <= release_date <= today + datetime.timedelta(
        days=RELEASE_INTERVAL)


# Given a list of tuples with (id, date), create a file a directory "New_Releases"
# (named with date ran) and write the new releases in order of newest first.
def write_new_releases(spotify: spotipy.Spotify, songs: list) -> None:
    fname = f'New_Releases_{datetime.datetime.today().__str__()}.txt'
    with open(os.path.join('New_Releases', fname), 'w') as file:
        for song in songs:
            track = spotify.album(song[0])
            line = f"{format_artists(track['artists'])} — {track['name']} ({song[1]})\n\t" \
                   f" {track['external_urls']['spotify']}\n\n"
            file.write(line)


# Formats a string for the names of Primary Artists given a list of artist names.
def format_artists(artists: []) -> str:
    a_name = ''
    for i in range(len(artists)):
        name = artists[i]['name']
        if i == 0:
            a_name += name
        elif i == len(artists) - 1:
            a_name += ' & ' + name
        else:
            a_name += ', ' + name
    return a_name


# Given a set of song ids, we return a list of tuples containing the id and the release date.
def add_release_date(spotify: spotipy.Spotify, song_ids: set) -> [("id, date")]:
    songs = []
    for song_id in song_ids:
        songs.append((song_id, datetime.date.fromisoformat(spotify.album(song_id)['release_date'])))
    return songs


if __name__ == '__main__':
    spotify = spotipy.Spotify(requests_timeout=100)  # can be changed depending on internet speed
    # spotify credentials can be added into the parameters for the Spotify object
    artist_ids = get_artists()
    song_ids = set()
    for artist_id in artist_ids:
        song_ids.update(check_new_music(spotify, artist_id))
    songs = add_release_date(spotify, song_ids)
    write_new_releases(spotify, sorted(songs, key=(lambda t: t[1]), reverse=True))
