data = [4, 5, 120, 121, 122, 123, 124, 125,
        126, 127, 128, 129, 130,
         131, 3, 132, 300, 400
        ]
min_valid = 100
max_valid = 200
stop = 0
# process the low values in the list
for index,value in enumerate(data):
    if  data[index] >= min_valid:
        stop = index + 1
        break  # line 10,11,12 is used to skip index greater than min_valid

print(stop) # for debugging
del data[:stop] #for deleting dATA IN stop
print(data)

# process the high values in the list
start = 0
for index in range(len(data)-1, -1, -1 ):
    
    if data[index] <= max_valid:
        start = index -1 # because numbers have been deleted 
        break

print(start)
del data[start:]
print(data)