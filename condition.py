age=int(input("How old are you? "))
if age >=18 and age <=65: #if 18<=age<=65
    print("have a nice day at work")
elif age<18:
    print("youre too young")
else:
    print("youre old... you should be retired")
if 18<=age>=65:
    print("not eligible to vote")
else:
    print("get voters card")