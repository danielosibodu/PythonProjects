parrot= "Norwegian Blue"
letter= input("Enter a character: ")
if letter in parrot:
    print("the {} is in {}".format(letter,parrot))
else: 
    print("I dint need that letter")