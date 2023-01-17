for index,character in enumerate("abcdefgh"):
    print(index + 1,character) # +1 because of index number always start from 0

for t in enumerate("abcdefgh"):
    index, character = t
    print(index,character)

index,character = (0,"a")
print(index)
print(character)