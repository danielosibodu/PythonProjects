name = input("Enter your name: ")
age =int(input("How old are you, {0}? ".format(name)))
print(age)
if age >= 18:
    print("Youre old enough to vote")
elif age >= 180:
    print("omo you supposed don die ".format(name))
else:
    print("Youre not old enough to vote. Please come back in {0} years".format (18-age))
#to comment many lines at ones press ctrl+ "/""