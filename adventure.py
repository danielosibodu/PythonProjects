available_exists = ["North", "East", "West", "South"]
chosen_exit = ""
while chosen_exit not in available_exists:
    chosen_exit = input("Please choose your direction: ")
    chosen_exit.casefold()
    if chosen_exit.casefold() == "quit":
        print("game over")
        break
    else:
        print("arent you glad you got out of there")
        break
