#Objective No.- 15
# Write a Python program to compute the number of characters, words and lines in a file

filename = input("Enter filename: ")

file = open(filename, "r")
content = file.read()

characters = len(content)
lines = content.count('\n') + 1 if content else 0
words = len(content.split())

print("Character count:", characters)
print("Word count:", words)
print("Line count:", lines)

file.close()
