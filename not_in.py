activity=input("what would you like to do today")
# if cinema not in activity:
#     print("i want to go the cinema")
if cinema not in activity.casefold():#casefold helps remove capital letters
    print("i want to go the cinema")