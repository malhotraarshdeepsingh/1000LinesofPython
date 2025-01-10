name = input("Enter your name: ")
print("Welcome to Python!", name)

# input() always returns a string
# To convert it into an integer, use int()
age = int(input("Enter your age: "))
print("You are", age, "years old")

# To convert it into a float, use float()
price = float(input("Enter the price: "))
print("The price is", price)

# To convert it into a boolean, use bool()
old = bool(input("Are you old? "))
print("You are old:", old)