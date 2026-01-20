#Name- Amrendra Kumar
#Regd. No.- 24E111B52
#Objective No.- 12
# Write a Python program to perform read and write operations on a file. 

file = open("sample.txt", "w")
content = input("Enter content to write in file: ")
file.write(content)
file.close()

file = open("sample.txt", "r")
data = file.read()
print("Content of file:")
print(data)
file.close()


