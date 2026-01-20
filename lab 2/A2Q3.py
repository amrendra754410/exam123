#Name- Rishit Swain
#Regd. No.- 24E119F02
#Objective No.- 3
# Write a Python program to access each character of string in forward and backward
# direction by using while loop

string = input("Enter a string: ")

i = 0
print("Forward direction:")
while i < len(string):
    print(string[i])
    i += 1

i = len(string) - 1
print("Backward direction:")
while i >= 0:
    print(string[i])
    i -= 1




