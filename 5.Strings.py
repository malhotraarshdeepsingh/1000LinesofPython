# Strings
# Strings are used in Python to record text information, such as name
# Strings in Python are actually a sequence, which basically means Python keeps track of every element in the string as a sequence

# Creating a String

# To create a string in Python you need to use either single quotes or double quotes. For example:
print("Hello")
print('Hello')

# Multiline Strings
# To create a multiline string, you can use triple quotes. For example:
print("""
Hello World!

This is a multiline string.
""")

# Accessing Characters
# You can access characters in a string using the index. For example:
a = "Hello, World!"
print(a[1]) # e

# Slicing Strings
# You can slice a string using the index. For example:
b = "Hello, World!"
print(b[2:5]) # llo

# String Concatenation
# To concatenate two strings you can use the + operator. For example:
c = "Hello"
d = "World!"
print(c + d) # HelloWorld!

# String Length
# To get the length of a string you can use the len() function. For example:
e = "Hello, World!"
print(len(e)) # 13

# String Methods
# There are many string methods in Python that you can use. For example:
f = "Hello, World!"

# upper() method converts a string to uppercase
print(f.upper()) # HELLO, WORLD!

# lower() method converts a string to lowercase
print(f.lower()) # hello, world!

# capitalize() method capitalizes the first character of a string
print(f.capitalize()) # Hello, world!

# count() method returns the number of occurrences of a substring in a string
print(f.count("o")) # 2

# find() method returns the index of the first occurrence of a substring in a string
print(f.find("o")) # 4

# replace() method replaces a substring in a string with another substring
print(f.replace("World", "Python")) # Hello, Python!

# split() method splits a string into a list of substrings based on a delimiter
print(f.split(",")) # ['Hello', ' World!']

# join() method joins a list of substrings into a string using a delimiter
g = ["Hello", "World!"]
print(" ".join(g)) # Hello World!

# format() method formats a string using placeholders
h = "Hello, {}!"
print(h.format("World")) # Hello, World!

# format_map() method formats a string using placeholders and a dictionary
i = "Hello, {name}!"
print(i.format_map({"name": "World"})) # Hello, World!

# isalpha() method checks if all characters in a string are alphabetic
j = "Hello"

if j.isalpha():
    print("All characters are alphabetic")
else:
    print("Not all characters are alphabetic")

# isdigit() method checks if all characters in a string are digits
k = "123"

if k.isdigit():
    print("All characters are digits")
else:
    print("Not all characters are digits")

# isalnum() method checks if all characters in a string are alphanumeric
l = "Hello123"

if l.isalnum():
    print("All characters are alphanumeric")
else:
    print("Not all characters are alphanumeric")

# isspace() method checks if all characters in a string are whitespace
m = "   "

if m.isspace():
    print("All characters are whitespace")
else:
    print("Not all characters are whitespace")

# isupper() method checks if all characters in a string are uppercase
n = "HELLO"

if n.isupper():
    print("All characters are uppercase")
else:
    print("Not all characters are uppercase")

# islower() method checks if all characters in a string are lowercase
o = "hello"

if o.islower():
    print("All characters are lowercase")
else:
    print("Not all characters are lowercase")

# startswith() method checks if a string starts with a substring
p = "Hello, World!"

if p.startswith("Hello"):
    print("String starts with 'Hello'")
else:
    print("String does not start with 'Hello'")

# endswith() method checks if a string ends with a substring
q = "Hello, World!"

if q.endswith("World!"):
    print("String ends with 'World!'")
else:
    print("String does not end with 'World!'")

# strip() method removes leading and trailing whitespace from a string
r = "   Hello, World!   "
print(r.strip()) # Hello, World!

# lstrip() method removes leading whitespace from a string
s = "   Hello, World!   "

print(s.lstrip()) # Hello, World!

# rstrip() method removes trailing whitespace from a string
t = "   Hello, World!   "

print(t.rstrip()) #   Hello, World!

# swapcase() method swaps the case of all letters in a string
u = "Hello, World!"

print(u.swapcase()) # hELLO, wORLD!

# title() method converts the first character of each word to uppercase and the remaining characters to lowercase in a string
v = "hello, world!"

print(v.title()) # Hello, World!

# zfill() method adds leading zeros to a string to make it a specified length
w = "42"

print(w.zfill(6)) # 000042

# center() method returns a centered string of a given length
x = "Hello, World!"

print(x.center(20)) #      Hello, World!

# ljust() method returns a left-justified string of a given length
y = "Hello, World!"

print(y.ljust(20)) # Hello, World!

# rjust() method returns a right-justified string of a given length
z = "Hello, World!"

print(z.rjust(20)) #      Hello, World!

# expandtabs() method replaces tab characters with a specified number of spaces
aa = "Hello\tWorld!"

print(aa.expandtabs(8)) # Hello         World!

# isidentifier() method checks if a string is a valid identifier
cc = "Hello"

if cc.isidentifier():
    print("Valid identifier")
else:
    print("Invalid identifier")

# isprintable() method checks if a string is printable
dd = "Hello, World!"

if dd.isprintable():
    print("String is printable")
else:
    print("String is not printable")

# isascii() method checks if all characters in a string are ASCII
ee = "Hello"

if ee.isascii():
    print("All characters are ASCII")
else:
    print("Not all characters are ASCII")

# encode() method encodes a string using a specified encoding
ff = "Hello, World!"

print(ff.encode("utf-8")) # b'Hello, World!'
print(ff.encode("utf-16")) # b'\xff\xfeH\x00e\x00l\x00l\x00o\x00,\x00 \x00W\x00o\x00r\x00l\x00d\x00!\x00'

# decode() method decodes a string using a specified encoding
gg = b'Hello, World!'

print(gg.decode("utf-8")) # Hello, World!

# maketrans() method returns a translation table to be used in translate() method
hh = "Hello, World!"

print(hh.translate(str.maketrans("Hello", "Bye"))) # Bye, World!

# partition() method splits a string into a tuple where the separator is the first occurrence of a substring
jj = "Hello, World!"

print(jj.partition(" ")) # ('Hello,', ',', ' World!')

# rpartition() method splits a string into a tuple where the separator is the last occurrence of a substring
kk = "Hello, World!"

print(kk.rpartition(" ")) # ('Hello, World!', '', '')

# splitlines() method splits a string into a list of substrings separated by newline characters
ll = "Hello\nWorld!"

print(ll.splitlines()) # ['Hello', 'World!']

# rsplit() method splits a string into a list of substrings separated by a delimiter from the right side
mm = "Hello, World!"

print(mm.rsplit(",", 1)) # ['Hello', 'World!']

# index() method finds the first occurrence of a substring in a string
oo = "Hello, World!"

print(oo.index("o")) # 4

# rindex() method finds the last occurrence of a substring in a string
pp = "Hello, World!"

print(pp.rindex("o")) # 7

# rfind() method returns the index of the last occurrence of a substring in a string
ss = "Hello, World!"

print(ss.rfind("o")) # 7