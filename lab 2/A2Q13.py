#Name- Amrendra Kumar
#Regd. No.- 24E111B52
#Objective No.- 13

filename = input("Enter filename: ")
n = int(input("Enter number of characters to reverse: "))

file = open(filename, "r")
content = file.read()
file.close()

part = content[:n]
reversed_part = part[::-1]
modified_content = reversed_part + content[n:]

file = open(filename, "w")
file.write(modified_content)
file.close()

print("File updated successfully.")
