# Tuples
# A tuple is a collection which is ordered and unchangeable. In Python tuples are written with round brackets.

# Creating a tuple
numbers = (1, 2, 3, 4, 5)
print(numbers)

# Accessing elements
print(numbers[0]) # 1

# Slicing
print(numbers[1:3]) # (2, 3)

# Negative indexing
print(numbers[-1]) # 5

# Concatenation
numbers = numbers + (6, 7, 8)
print(numbers)

# Immutable
# numbers[0] = 10 # TypeError: 'tuple' object does not support item assignment

# Length of a tuple
print(len(numbers)) # 8

# Checking if an element exists in a tuple
print(1 in numbers) # True
print(10 in numbers) # False
