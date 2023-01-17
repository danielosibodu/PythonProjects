album = [("Welcome to my Nightmare", "Alice Cooper", 1975),
         ("Bad Company", "Bad Company", 1974),
         ("Nightflight", "Budgie", 1981),
         ("More Mayhem", "Emilda May", 2011),
         ("Ride the Lightning", "Metallica", 1984),
         ]
        # if the brackets are removed then the list will be 15
print(len(album))
for alb in album:
    print("Album: {}, Artist: {}, Year: {}"
          .format(alb[0],alb[1],alb[2]))
# or 
for name,artist,year in album:
    print("Album: {}, Artist: {}, Year: {}"
          .format(name,artist,year))
