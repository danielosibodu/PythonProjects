#         012456789
parrot = "Norwegian"
print(parrot)
print(parrot[3])#fourth position
print()
character = "unstoppable"
print(character[0])
print(character[1])
print(character[2])
print(character[3])
print(character[4])
print(character[5])
print()
print(character[-1])#will print backwards
#or
print(character[5-6])#minus the position from the array
print()
print(character[0:6])#from zeroth positon to the sixth position
print(character[3:5])
print(character[:6])#prints from start to sixth position
print(character[0:])#prints from start to finish
print()
print(character[:2 + 4:])
print(character[:])#prints all
print()
print(character[-4:-2])#you can only use negative slicing from front to back
print(character[-4:10])
print(character[0:6:2])#"we win" will print in steps of 2
print(character[1::2])#skips the first postion and takes 2 steps
