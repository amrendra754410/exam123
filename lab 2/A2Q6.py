#Name- Rishit Swain
#Regd. No.- 24E119F02
#Objective No.- 6

n = int(input("Enter the size of the list: "))
numbers = []

for i in range(n):
    element = int(input("Enter element: "))
    numbers.append(element)

maximum = max(numbers)
print("Maximum element:", maximum)


