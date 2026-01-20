#Name- Amrendra Kumar
#Regd. No.- 24E111B52
#Objective No.- 14

import string

filename = input("Enter filename: ")

file = open(filename, "r")
for line in file:
    words = line.split()
    for word in words:
        word = word.strip()
        word = word.strip(string.punctuation)
        word = word.lower()
        print(word)
file.close()


