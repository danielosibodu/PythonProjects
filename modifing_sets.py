# numbers = {}    # this is a dict type
# numbers = {*{}} # this is set type
# numbers = {*""} # this is a set type
# numbers = set() # this a set type

# numbers = set()
# numbers.add(1)
# print(numbers)
#
# while len(numbers) < 4:
#     next_value = int(input('Enter your next value: '))
#     numbers.add(next_value)
# print(numbers)

data = ['blue', 'red', 'blue', 'green', 'red', 'blue',  'white']
# create a set from the list to remove duplicates
unique_data = sorted(set(data))
print(unique_data)

# creating a list of unique colours, keeping the order they appear
unique_data = list(dict.fromkeys(data))
print(unique_data)

print()
print(dict.fromkeys(data))
