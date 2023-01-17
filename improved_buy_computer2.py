available_parts = ['computer',
                   'monitor',
                   'keyboard',
                   'mouse',
                   'mouse pad',
                   'hdmi cable',
                   'loudspeakers',
                   'microphones'
                  ]
# valid_choice = [str(i) for i in range(1,len(available_parts)+1)]
valid_choice = []
for i in range(1,len(available_parts) + 1):
    valid_choice.append(str(i))
print(valid_choice)
current_choice = "-"
computer_parts = []

while current_choice != "0":
    if current_choice in valid_choice:
        
        index=int(current_choice) - 1
        chosen_parts=available_parts(index)
        if chosen_parts in computer_parts:
            print("removing {}".format(current_choice))
            chosen_parts.remove(computer_parts)
        else:
            print("Adding {}".format(current_choice))
            chosen_parts.append(computer_parts)
            print("the lists available are: {}".format(computer_parts))
            computer_parts.append(chosen_part) 
    else:
        print("Please add options from the list below")
        for number,parts in enumerate(available_parts):
            print("{0}: {1}".format(number + 1,parts))
    current_choice = input()

print(computer_parts)
