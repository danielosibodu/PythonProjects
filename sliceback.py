#         01234567890123456789012345
letters ="abcdefghijklmnopqrstuvwxyz"
#         65432109876543210987654321                     
backwards=letters[25:0:-1]#wont print everything. stops at b 
backwards=letters[25::-1]#prints everything. if stop value is added it wont be able to print it all 
print(backwards)
#or
backwards=letters[::-1]#prints everything by a negative step
print()
backwards=letters[16:13:-1]#qpo
print(backwards)
backwards=letters[4::-1]#prints edcba
print(backwards)
backwards=letters[-1:-9:-1]#prints zyxwvuts
print(backwards)
#or
backwards=letters[:-9:-1]#prints zyxwvuts
print(backwards)
print()
backwards=letters[-4:]#prints wxyz
print(backwards)
backwards=letters[-1:]#prints z
print(backwards)
backwards=letters[:1]#prints a
print(backwards)