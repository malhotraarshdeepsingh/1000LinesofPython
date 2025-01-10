# Loops

# For loop
for i in range(10):
    print(i)

# While loop
i = 0
while i < 10:
    print(i)
    i += 1

# Break statement
for i in range(10):
    if i == 5:
        break
    print(i)

# Continue statement
for i in range(10):
    if i == 5:
        continue
    print(i)

# Nested loops
for i in range(10):
    for j in range(10):
        print(i, j)

# Infinite loop
while True:
    print("Hello World")

# Loop over a list
numbers = [1, 2, 3, 4, 5]
for number in numbers:
    print(number)

# Loop over a dictionary
person = {
    "name": "John",
    "age": 30,
    "city": "New York"
}

for key, value in person.items():
    print(key, ":", value)

# Loop over a set
numbers = {1, 2, 3, 4, 5}
for number in numbers:
    print(number)

# Loop over a tuple
numbers = (1, 2, 3, 4, 5)
for number in numbers:
    print(number)

# Loop over a string
name = "John"
for letter in name:
    print(letter)

# Loop over a range
for i in range(10):
    print(i)

# Loop over a range with a step
for i in range(1, 10, 2):
    print(i)

# Loop over a reversed list
numbers = [1, 2, 3, 4, 5]
for number in reversed(numbers):
    print(number)

# Loop over a reversed string
name = "John"
for letter in reversed(name):
    print(letter)

# Loop over a reversed range
for i in reversed(range(10)):
    print(i)

# Loop over a sorted list
numbers = [5, 3, 1, 4, 2]

# Sorting in ascending order
for number in sorted(numbers):
    print(number)

# Sorting in descending order
for number in sorted(numbers, reverse=True):
    print(number)

# Loop over a sorted string
name = "John"
for letter in sorted(name):
    print(letter)

# Loop over a sorted range
for i in sorted(range(10), reverse=True):
    print(i)

# Loop over a dictionary with sorted keys
person = {
    "name": "John",
    "age": 30,
    "city": "New York"
}

for key in sorted(person.keys()):
    print(key, ":", person[key])
