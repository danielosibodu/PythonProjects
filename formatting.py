for i in range(1,13):
    print("No. {0} squared is {1} and cubed is {2}".format(i,i**2,i**3))

for i in range(1,13):
    print("No. {0:2} squared is {1:3} and cubed is {2:4}".format(i,i**2,i**3))#the :2 or :4 gives it more width
print()
for i in range(1,13):
    print("No. {0:2} squared is {1:^3} and cubed is {2:^4}".format(i,i**2,i**3))# middle allignment
print()
for i in range(1,13):
    print("No. {0:2} squared is {1:>3} and cubed is {2:>4}".format(i,i**2,i**3))#right alignment
print()

for i in range(1,13):
    print("No. {0:2} squared is {1:<3} and cubed is {2:<4}".format(i,i**2,i**3))##left alignment
print()
print("Pi is approximately {0:<12}".format(22/7))
print("Pi is approximately {0:<12f} ".format(22/7))
print("Pi is approximately {0:<12} ".format(22/7))
print("Pi is approximately {0:12} ".format(22/7))
print("Pi is approximately {0:<72.50f} ".format(22/7))
print("Pi is approximately {0:12} ".format(22/7))

print()
for i in range(1,13):
    print("No. {} squared is {} and cubed is {:4}".format(i,i**2,i**3))