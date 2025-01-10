# Write a Python program to read an entire text file.
file = open("test.txt", "r")

# Print the content of the file
print(file.read())

# Close the file
file.close()



# Write a Python program to read first n lines of a file.
file = open("test.txt", "r")

# Read the first 5 lines
lines = file.readlines()[:5]
print(lines)

# Close the file
file.close()


# Write a Python program to read last n lines of a file.
file = open("test.txt", "r")

# Get the total number of lines in the file
total_lines = len(file.readlines())

# Read the last 5 lines
file.seek(0)
lines = file.readlines()[total_lines-5:]
print(lines)

# Close the file
file.close()


# Write a Python program to count the number of occurrences of a given word in a file.
file = open("test.txt", "r")

# Read the content of the file
content = file.read()

# Convert the content to lowercase
content = content.lower()

# Split the content into words
words = content.split()

# Count the occurrences of the given word
word = "python"
count = words.count(word)
print(f"The word '{word}' occurs {count} times in the file.")

# Close the file
file.close()


# Write a Python program to count the number of occurrences of each word in a file.
file = open("test.txt", "r")

# Read the content of the file
content = file.read()

# Convert the content to lowercase
content = content.lower()

# Split the content into words
words = content.split()

# Count the occurrences of each word
word_count = {}

for word in words:
    if word in word_count:
        word_count[word] += 1
    else:
        word_count[word] = 1

# Print the word count
for word, count in word_count.items():
    print(f"'{word}': {count}")

# Close the file
file.close()

# Write a Python program to remove all duplicate lines from a file.
file = open("test.txt", "r")
lines = file.readlines()
file.close()

file = open("test.txt", "w")
lines_set = set(lines)

for line in lines_set:
    file.write(line)
    file.write("\n")

file.close()


# Write a Python program to find the longest word in a file.
file = open("test.txt", "r")

# Read the content of the file
content = file.read()

# Convert the content to lowercase
content = content.lower()

# Split the content into words
words = content.split()

# Find the longest word
longest_word = max(words, key=len)
print(f"The longest word in the file is '{longest_word}'.")

# Close the file
file.close()


# Write a Python program to reverse the order of words in a file
file = open("test.txt", "r")

# Read the content of the file
content = file.read()

# Convert the content to lowercase
content = content.lower()

# Split the content into words
words = content.split()

# Reverse the order of words
reversed_words = " ".join(reversed(words))
print(reversed_words)

# Close the file
file.close()


# Write a Python code to open a file in both modes simultaneously
file = open("test.txt", "r+w")

# Read and write the content of the file
content = file.read()

# Modify the content
content = content.upper()

# Write the modified content back to the file
file.seek(0)
file.write(content)

# Append a new line to the file
file.write("\nThis is a new line.")

# Read the content again to verify the modifications
modified_content = file.read()
print(modified_content)

# Close the file
file.close()


# Deleting a file
import os

# Check if the file exists
if os.path.exists("test.txt"):
    # Delete the file
    os.remove("test.txt")
    print("File deleted successfully")
