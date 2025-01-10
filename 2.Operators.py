# Operators

# Arithmetic Operators
# (+, /, -, *, %, **)

# Comparison Operators
# (==, !=, >, <, >=, <=)

# Logical Operators
# (and, or, not)

# Assignment Operators
# (=, +=, -=, *=, /=, %=, **=)

# Bitwise Operators
# (&, |, ^, ~, <<, >>)

# Membership Operators
# (in, not in)

# Identity Operators
# (is, is not)

# Arithmetic Operators
a = 10
b = 20
print(a + b) # 30 addition
print(a - b) # -10 subtraction
print(a * b) # 200 multiplication
print(a / b) # 0.5 division
print(a % b) # 10 modulo (remainder)
print(a ** b) # 100000000000000000000 exponentiation


# Comparison Operators
a = 10
b = 20
print(a == b) # False
print(a != b) # True
print(a > b) # False
print(a < b) # True
print(a >= b) # False
print(a <= b) # True


# Logical Operators
a = True
b = False
print(a and b) # False
print(a or b) # True
print(not a) # False


# Assignment Operators
a = 10
b = 20
a += b # a = a + b
print(a) # 30
a -= b # a = a - b
print(a) # 10
a *= b # a = a * b
print(a) # 200
a /= b # a = a / b
print(a) # 10
a %= b # a = a % b
print(a) # 10
a **= b # a = a ** b
print(a) # 100000000000000000000


# Bitwise Operators
a = 10
b = 20
print(a & b) # 0  bitwise AND
print(a | b) # 30 bitwise OR
print(a ^ b) # 30 bitwise XOR
print(~a) # -11 bitwise NOT
print(a << b) # 100000000000000000000000  1 bitwise left shift
print(a >> b) # 0  1 bitwise right shift


# Membership Operators
a = "Hello World!"
print("Hello" in a) # True
print("Hello" not in a) # False


# Identity Operators
a = 10
b = 10
print(a is b) # True
print(a is not b) # False
