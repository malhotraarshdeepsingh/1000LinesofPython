# Set
# It is a collection of unordered items
# Each element in set must be unique and immutable

# Creating a set
numbers = {1, 2, 3, 4, 5}
print(numbers)

# Adding elements to a set
numbers.add(6)
print(numbers)

# Removing elements from a set
numbers.remove(6)
print(numbers)

# Checking if an element exists in a set
print(1 in numbers) # True

# Union of two sets
numbers1 = {1, 2, 3}
numbers2 = {4, 5, 6}
union = numbers1.union(numbers2)
print(union)

# Intersection of two sets 
intersection = numbers1.intersection(numbers2)
print(intersection)

# Difference of two sets
difference = numbers1.difference(numbers2)
print(difference)

# Difference of two sets in reverse order
difference = numbers2.difference(numbers1)
print(difference)

# Symmetric difference of two sets
symmetric_difference = numbers1.symmetric_difference(numbers2)
print(symmetric_difference)

# Removing duplicates from a list
numbers = [1, 2, 3, 4, 5, 1, 2, 3]

# Convert list to set to remove duplicates
unique_numbers = set(numbers)
print(unique_numbers)

# Convert set back to list
unique_numbers = list(unique_numbers)
print(unique_numbers)

# Set comprehension
numbers = {x for x in range(1, 6)}

# Convert set to list
numbers = list(numbers)
print(numbers)

# Nested set
set1 = {1, 2, 3}
set2 = {4, 5, 6}
nested_set = {set1, set2}
print(nested_set)


# Set operations on nested sets
set1 = {1, 2, 3}
set2 = {4, 5, 6}

nested_set1 = {set1, set2}
nested_set2 = {2, 3, 4}
nested_set3 = {5, 6, 7}
nested_set4 = {set1, nested_set2, nested_set3}

union = nested_set1.union(nested_set4)
print(union)

intersection = nested_set1.intersection(nested_set4)
print(intersection)

difference = nested_set1.difference(nested_set4)
print(difference)

symmetric_difference = nested_set1.symmetric_difference(nested_set4)
print(symmetric_difference)


# Nested set comprehension
nested_set = {frozenset({x, x + 1}) for x in range(5)}
print(nested_set)

# Set operations on nested frozensets
nested_set1 = {frozenset({1, 2}), frozenset({3, 4})}
nested_set2 = {frozenset({2, 3}), frozenset({4, 5})}
nested_set3 = {frozenset({5, 6}), frozenset({7, 8})}
nested_set4 = {nested_set1, nested_set2, nested_set3}

union = nested_set1.union(nested_set4)
print(union)

intersection = nested_set1.intersection(nested_set4)
print(intersection)

difference = nested_set1.difference(nested_set4)
print(difference)

symmetric_difference = nested_set1.symmetric_difference(nested_set4)
print(symmetric_difference)
