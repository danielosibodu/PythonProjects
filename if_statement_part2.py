import random
highest=10
answer=random.randint(1, highest)

print("Enter your guess between 1 and {}".format(highest))
guess=int(input())

# if guess > answer:3
#     print("higher")
#     guess = int(input())
#     if guess==answer:
#         print("you guessed it right")
#     else:
#         print("youvw not guessed correctly")
# elif guess < answer:
#     print("lower")
#     if guess==answer:
#         print("you guessed it right")
#     else:
#         print("youvw not guessed correctly") jmk,./
# else:
#     print("you got it right")

if guess==answer:
    print("you got it first try")
else:
    if guess > answer:
        print("guess lower")
    else:
        print("guess higher")
    guess=int(input())
    if guess!=answer:
        print("you guessed it wrong")
    else:
        print("you guessed right")
        print(answer)# TODO: Remove after testing