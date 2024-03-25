# Defining some data, using a list with tuples containing lists
albums = [
    ("Welcome to my Nightmare", "Alice Cooper", 1975,
     [
         (1, "Welcome to my Nightmare"),
         (2, "Devil's Food"),
         (3, "The Black Widow"),
         (4, "Some Folks"),
         (5, "Only Women Bleed"),
     ]
     ),
    ("Bad Company", "Bad Company", 1974,
     [
         (1, "Can't Get Enough"),
         (2, "Rock Steady"),
         (3, "Ready for Love"),
         (4, "Don't Let Me Down"),
         (5, "Bad Company"),
         (6, "The Way I Choose"),
         (7, "Movin' On"),
         (8, "Seagull"),
     ]
     ),
    ("Nightflight", "Budgie", 1981,
     [
         (1, "I Turned to Stone"),
         (2, "Keeping a Rendezvous"),
         (3, "Reaper of the Glory"),
         (4, "She Used Me Up"),
     ]
     ),
    ("More Mayhem", "Imelda May", 2011,
     [
         (1, "Pulling the Rug"),
         (2, "Psycho"),
         (3, "Mayhem"),
         (4, "Kentish Town Waltz"),
     ]
     ),
]

# Unpacking the tuples in the list
for name, artist, year, song in albums:
    print("Album: {}, Artist: {}, Year: {}, Song: {}"
           .format(name, artist, year, song))

# Printing out details of a specific album
album = albums[2]
print(album)

# Printing out all songs in the album
songs = album[3]
print(songs)

# Printing out a specific song
song = songs[3]
print(song)

# Accessing a particular nested song through indexing
mayhem = albums[3][3][2][1]
print(mayhem)
