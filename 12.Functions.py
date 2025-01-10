# Functions

def greet_user(name):
    """Print a greeting message."""
    print(f"Hello, {name}!")

greet_user("John Doe") # Hello, John Doe!



def print_list(list):
    """Print all items of the list in one line."""
    for item in list:
        print(item, end=" ")

cities = ["New York", "Los Angeles", "Chicago"]
print_list(cities)
# Output:- New York Los Angeles Chicago


def factorial(number):
    """Calculate the factorial of a number."""
    if number <= 0:
        return 1
    else:
        return number * factorial(number - 1)

print(factorial(5)) # 120

