t = ("a", "b", "c") # or "a", "b", "c" 
print(t) # bracket parenthesis is optional  

welcome = "Welcome to my Nightmare", "Alice Cooper", 1975
bad = "Bad Company", "Bad Company", 1974
budgie = "Nightflight", "Budgie", 1981
imelda = "More Mayhem", "Emilda May", 2011
metallica = "Ride the Lightning", "Metallica", 1984
print(metallica)
print(metallica[0])
print(metallica[1])
print(metallica[2])

metallica2 = list(metallica) # turning mettalica to list so we can append a value to the tuple metallica
print(metallica2)

metallica2[0] = "Master of Puppets"
print(metallica2) 
print()
title, artist, year = metallica
print(title)
print(artist)
print(year)
print()

table = ("coffee table", 200, 100, 75, 34.50)
print(table[1]*table[2]) # it wont be easier when a lot of values are in the tuple
name, length, width, height, price = table
print(length * width)