# Importing required module for hashing
import hashlib

# Look into algorithms guaranteed to exist in all Python implementations and available algorithms
print(sorted(hashlib.algorithms_guaranteed))
print()
print(sorted(hashlib.algorithms_available))

python_program = """for i in range (10):
print(i)
"""
print(python_program)

# Look into each byte in the byte array used in the hashing function
# We can then see what character each number represents, for example 112 is an f and 10 is a line break
for b in python_program.encode('utf8'):
    print(b, chr(b))

# Creating a hash value using the SHA256 hashing function
# The hexdigest method produces a hexadecimal representation of the secure hash
# This is just a 256 bit, or 32 bytes, number. SHA256 produces 256 bit numbers.
original_hash = hashlib.sha256(python_program.encode('utf8'))
print(f"SHA256: {original_hash.hexdigest()}")

# Using the hash value to see if the input data has been changed
# This is done by appending some new code to the input data
python_program += "print('code change')"
print(python_program)

new_hash = hashlib.sha256(python_program.encode('utf8'))
print()
print(f"SHA256: {new_hash.hexdigest()}")

# Get the program to check the hashes for us
if new_hash.hexdigest() == original_hash.hexdigest():
    print("The code has not been changed")
else:
    print("The code has been modified")
