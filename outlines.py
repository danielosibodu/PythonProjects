data = [4, 5, 120, 121, 122, 123, 124, 125,
        126, 127, 128, 129, 130, 131, 132 
        ]

del data[0:2]
print(data)
# when you delete a charater, the other characters move up 
# for instance 4 and 5 are deleted
# 120 and 121 are now first and second respectively 
# the other characters follows
del data[14:]# it would print because slice '14' is out of the list
print(data)
del data[12:] # will print everything except 132
print(data)

