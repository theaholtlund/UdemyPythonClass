# Importing required modules
import os
import fnmatch


# Defining a generator function to find albums
# The songs listed in the function are not actually available, so this code will not work
def find_albums(root, artist_name):
    caps_name = artist_name.upper()
    for path, directories, files in os.walk(root):
        # for artist in fnmatch.filter(directories, artist_name):
        # for artist in fnmatch.filter((d.upper() for d in directories), caps_name):
        for artist in (d for d in directories if fnmatch.fnmatch(d.upper(), caps_name)):
            subdir = os.path.join(path, artist)
            for album_path, albums, _ in os.walk(subdir):
                for album in albums:
                    yield os.path.join(album_path, album), album


# Defining a second generator function, which takes the output from the first iterator function as the argument
def find_songs(albums):
    for album in albums:
        for song in os.listdir(album[0]):  # We want the path, not the name of the album
            yield song


# Defining variables for the function outputs
album_list = find_albums("music", "black*")
song_list = find_songs(album_list)

for s in song_list:
    print(s)
