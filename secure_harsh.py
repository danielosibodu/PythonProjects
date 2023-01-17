import hashlib

# print(sorted(hashlib.algorithms_available))
# print(sorted(hashlib.algorithms_guaranteed))

python_program = """for i in range(10):
print(i)
"""
print(python_program)

# for b in python_program.encode('utf8'):
#     print(b, chr(b))

original_hash = hashlib.sha256(python_program.encode('utf8'))
print(f'sha256: {original_hash.hexdigest()}')

python_program += """orint('code changed)"""
print(python_program)

new_hash = hashlib.sha256(python_program.encode('utf8'))
print()
print(f'sha256: {new_hash.hexdigest()}')
if original_hash.hexdigest() == new_hash.hexdigest():
    print("the code hasnt been modified")
else:
    print('code has been modiified')