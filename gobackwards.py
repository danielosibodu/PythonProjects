data = [4, 5, 120, 121, 122, 123, 124, 125,
        126, 127, 128, 129, 130,
         131, 3, 132, 300, 400
        ]
min_valid = 100
max_valid = 200
for index in range(len(data) - 1, -1, -1 ):
    if data[index] < min_valid or data[index] > max_valid:
        print(index +1 ,data)
        del data[index]
print(data)