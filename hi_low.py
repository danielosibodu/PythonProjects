low=1
high=1000
print("think of a number between{} and {}".format(low,high))
input("press enter to start the game")
guesses=1
while True:
    print("\t Guessing numbers between {} and {}".format(low,high))
    guess = low + (high-low)//2
    high_low= input("My guess is {}. Should I guess higher or lower?"
                    "Enter h or l or  c if my guess was correct "
                    .format(guess)).casefold()

    if high_low == "h":
        low=guess+1
    elif high_low == "l":
        high=guess-1
    else:
        if high_low == "c":
            print("the guess was correct")
            print("you got it in {} guesses".format(guesses))
    
    guesses=guesses+1