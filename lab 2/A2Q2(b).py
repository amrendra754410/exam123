#Name- Amrendra Kumar
#Regd. No.- 24E111B52
#Objective No.- 2(b)

string = input("Enter a string: ")
sum = 0
for ch in string:
    if ch.isdigit():
        sum += int(ch)
print("Sum of digits:", sum)



