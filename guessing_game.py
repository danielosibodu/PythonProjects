import random
highest=10
answer=random.randint(1,highest)
print("If you want no part of the game press '0'")
print("Enter your guess from 1 to {}".format(highest))
guess=int(input())
while guess!=answer:
    if guess==0:
        print("I quit")
        break
    if guess==answer:
        print("you got it right first time")
    else:
        if guess < answer:
            print("higher")
        else:
            print("lower")
        guess=int(input("Guess again: "))
        if guess != answer:
            print("you got the guess wrong")
        else: 
            print("took you long enough")
else:
    print("You got it!!!.The answer is {}.".format(answer))