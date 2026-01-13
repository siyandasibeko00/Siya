class Album():
    def __init__(self, album_name, number_of_songs, album_artist):
        self.album_name = album_name
        self.number_of_songs = number_of_songs
        self.album_artist = album_artist

    def __str__(self):
        return f"Album name: {self.album_name}, Album artist: {self.album_artist}, Number of songs: {self.number_of_songs}"
    
albums1 = [
   Album("Sgt. Pepper's Lonely Hearts Cub Band", "The Beatles", 13),
  Album("Thriller", "Michael Jackson", 9),
  Album("Nevermind", "Nirvana", 12),
  Album("Songs in the Key of Life", "Stevie Wonder", 21),
  Album("What's Going On", "Marvin Gaye", 9)
]

for album in albums1:
  print(album)

albums1.sort(key=lambda music: music.number_of_songs)

for album in albums1:
  print(album)

albums1[1], albums1[2] = albums1[2], albums1[1]

for album in albums1:
  print(album)

albums2 = []

albums2 = [
Album("The Miseducation of Lauryn Hill", "Lauryn Hill", 14),
  Album("Enter the Wu-Tang (36 Chambers)", "Wu-Tang Clan", 12),
  Album("My Beautiful Dark Twisted Fantasy", "Kanye West", 13),
  Album("To Pimp a Butterfly", "Kendrick Lamar", 16),
  Album("The Low End Theory", "A Tribe Called Quest", 13)
]

for album in albums2:
  print(album)

albums2.extend(albums1)

for album in albums2:
  print(album)

albums2.append(Album("Dark Side of the Moon', 'Pink Floyd", 9))
albums2.append(Album("Oops!... I did it Again", "Britney Spears", 16))

albums2.sort(key=lambda music: music.album_name)

for album in albums2:
  print(album)

for i, album in enumerate(albums2):
  if album.album_name == "Dark Side of the Moon":
    print(f"Index of Dark Side of the Moon: {i}")