# Dictionary
# Dictionary is a collection of key-value pairs

# Creating a dictionary
person = {
    "name": "John",
    "age": 30,
    "city": "New York"
}

# Accessing values
print(person["name"]) # John
print(person["age"]) # 30
print(person["city"]) # New York

# Updating values
person["age"] = 40

# Deleting a key-value pair
del person["city"]

# Checking if a key exists in the dictionary
if "name" in person:
    print(person["name"]) # John
else:
    print("Name not found")

# Adding a new key-value pair
person["country"] = "USA"

# Printing the updated dictionary

for key, value in person.items():
    print(key, ":", value)

# Output:
# name : John
# age : 40
# city: New York
# country : USA

# Dictionary Methods

# keys()
# Returns a list of all keys in the dictionary
print(person.keys()) # dict_keys(['name', 'age', 'country'])

# values()
print(person.values()) # dict_values(['John', 40, 'USA'])

# items()
print(person.items()) # dict_items([('name', 'John'), ('age', 40), ('country', 'USA')])

# get()
# Returns the value of a key
print(person.get("name")) # John

# copy()
# Returns a copy of the dictionary
person_copy = person.copy()
print(person_copy) # {'name': 'John', 'age': 40, 'country': 'USA'}

# pop()
person.pop("name")
print(person) # {'age': 40, 'country': 'USA'}

# popitem()
person.popitem()
print(person) # {'age': 40}

# setdefault()
person.setdefault("name", "John")
print(person) # {'age': 40, 'name': 'John'}

# update()
person.update({"city": "New York"})
print(person) # {'age': 40, 'name': 'John', 'city': 'New York'}

# fromkeys()
# Creates a new dictionary with the specified keys and values
person = dict.fromkeys(["name", "age", "city"], "Unknown")
print(person) # {'name': 'Unknown', 'age': 'Unknown', 'city': 'Unknown'}

# len()
# Returns the number of key-value pairs in the dictionary
print(len(person)) # 3

# clear()
# Removes all key-value pairs from the dictionary
person.clear()
print(person) # {}
