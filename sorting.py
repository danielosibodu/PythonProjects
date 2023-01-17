pangram = "The quick brown fox jumps over the lazy dog"
letter = sorted(pangram)
print(letter)
numbers = [3.3, 4.2, 4.1, 8.7, 9.3, 5.3]
print(sorted(numbers))
# difference between sort and sorted
# sort will rearrange the list and has no return value
# sorted will give it a new value and it has a return value
numbers.sort()
print(numbers)
missing_letter = sorted("The quick brown fox jumps over the lazy dog",key=str.casefold)
print(missing_letter) 
names = ["mary",
         "Dnaiel"
         "James"
         "dan"
         "john"
         ]
names.sort(key=str.casefold)