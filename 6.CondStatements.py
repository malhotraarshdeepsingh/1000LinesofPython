# if, elif, else statements

light = "yellow"

if light == "green":
    print("Go")
elif light == "yellow":
    print("Slow Down")
elif light == "red":
    print("Stop")
else:
    print("Invalid Light Color")

# Output:
# Slow Down


# Nested if statements

age = 70

if age >= 18:
    print("Adult")
    if age >= 65:
        print("Senior Citizen")
    else:
        print("Not a Senior Citizen")
else:
    print("Minor")

# Output:
# Senior Citizen


# Ternary Operator

light = "yellow"
message = "Go" if light == "green" else "Slow Down"
print(message)

# Output:
# Slow Down

age = 70
message = "Adult" if age >= 18 else "Minor"
print(message)

# Output:
# Adult
