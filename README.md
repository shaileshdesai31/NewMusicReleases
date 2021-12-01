# NewMusicReleases

--- USAGE NOTES ---
  - General use is to btain various information from the Spotify API about artists, songs, and albums.
  
  - The primary file is the new-music-checker.py script. The script generates a file
    with all the new releases for the artists in the "artists.txt" files. The "artists.txt"
    that is available is an example to show how file should be formatted. Any artists can be added.
    (See each file to understand how they specifically work.)
    
  - The fill_artists_file.py simply uses a playlist on spotify to add artists to the artists.txt file
    so that the user doesn't need to add them manually. For example, if the user is interested in
    finding new releases for classic rock, they could use a classic rock playlist on spotify to fill
    the artists.txt file with artists on songs in said playlist.
    
  - All other files are not used in the new-music-checker.py script and serve other purposes such as
    obtaining cover art and obtaining recent releases for a certain artist (intro concpet to new-music-checker.py).
    
--- INSTALLATIONS ---

In order to use any of these scripts, the user must mainly download the spotipy library.
Depending on which file being run, there may be different other libraries used, but the main
library is the spotipy library. Other used libraries consist of datetime, spotipy.oauth2, and os.

--- CREDITS ---
All files written by Shailesh Desai. The python spotipy library was used throughout all files.
The spotipy library tutorials to structure some small generic tasks in some files.
