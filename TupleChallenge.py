imelda = "More Mayhem", "imelda may", 2011, ((1, "Pulling the Rug"), (2, "Psycho"), (3, "Mayhem"), (4, "Kentish Town"))

album, artist, year, tracks = imelda

print(album)
print(artist)
print(year)
print("\tTracks Listing")
for songs in tracks:
    track, song = songs
    print("\t{}. {}".format(track, song))


