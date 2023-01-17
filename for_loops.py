# parrot = "Norwegian Blue"
# for character in parrot:
#     print(character)

# number=input("pleae enter the number, using any seperator ")
number="1, 439,422,43255"
seperator=""
for char in number:
    if char.isnumeric():#number will be added to seperator. or if not char is.numeric():- ","and" "will added to seperator
        seperator=seperator+char
print(seperator)