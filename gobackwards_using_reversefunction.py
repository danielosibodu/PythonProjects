data = [4, 5, 120, 121, 122, 123, 124, 125,
        126, 127, 128, 129, 130,
         131, 3, 132, 300, 400
        ]
min_valid = 100
max_valid = 200
top_index = len(data) - 1 # for items to retain original index
for index,value in enumerate(reversed(data)):
    if data[index] < min_valid or data[index] > max_valid:
        print(top_index-index+1,value) 
        del data[top_index-index]
    

print(data)