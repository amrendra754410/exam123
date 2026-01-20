#Name- Rishit Swain
#Regd. No.- 24E119F02
#Objective No.- 3

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




