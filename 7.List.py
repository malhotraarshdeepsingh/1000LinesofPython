# List 
# a built in data structure in python
# it is a collection of data structures

# Creating a list
numbers = [1, 2, 3, 4, 5]
print(numbers)

# Length of a list
print(len(numbers)) # 5

# Concatenating lists
numbers = numbers + [6, 7, 8]
print(numbers)

# Repeating elements in a list
numbers = numbers * 2
print(numbers)

# Checking if an element exists in a list
1 in numbers # True
'a' in numbers # False

# Accessing elements in a list using negative indices
print(numbers[-1]) # 8
print(numbers[-2]) # 7

# Accessing elements in a list
print(numbers[0]) # 1
print(numbers[1]) # 2

# Updating elements in a list
numbers[0] = 10

# Adding elements to a list
numbers.append(6)
print(numbers)

# Removing elements from a list
numbers.remove(6)
print(numbers)

# List slicing
print(numbers[1:3]) # [2, 3]

# List methods
numbers.append(6)
print(numbers)

numbers.sort()
print(numbers)

numbers.reverse()
print(numbers)

numbers.pop()
print(numbers)

numbers.insert(0, 1)
print(numbers)

numbers.extend([7, 8])
print(numbers)

numbers.clear()
print(numbers)

# List comprehension
squares = [x ** 2 for x in range(10)]

print(squares)

# Nested lists
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

print(matrix[0]) # [1, 2, 3]
print(matrix[1]) # [4, 5, 6]
print(matrix[2]) # [7, 8, 9]

print(matrix[0][0]) # 1
print(matrix[1][1]) # 5
print(matrix[2][2]) # 9

# Lists can even contain different types of data
mixed = [1, 'a', 2.5, True]

print(mixed) # [1, 'a', 2.5, True]

# Lists are mutable
a = [1, 2, 3]
b = a
b[0] = 10

print(a) # [10, 2, 3]

# Lists are not immutable
a = [1, 2, 3]
b = a
b = [10, 20, 30]

print(a) # [1, 2, 3]

# Lists can contain other lists
a = [1, 2, 3]
b = [4, 5, 6]
c = [a, b]

print(c) # [[1, 2, 3], [4, 5, 6]]

# Lists can be nested indefinitely
a = [1, 2, [3, 4, [5, 6]]]

print(a[2][2][0]) # 5

# List comprehension with conditions
even = [x for x in range(10) if x % 2 == 0]

print(even) # [0, 2, 4, 6, 8]

# List comprehension with multiple conditions
even = [x for x in range(10) if x % 2 == 0 if x % 3 == 0]

print(even) # [0]

# List comprehension with nested conditions
even = [x for x in range(10) if x % 2 == 0 if x % 3 == 0]

print(even) # [0]

