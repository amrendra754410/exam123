#Objective No.- 6
# Write a Python program to enter elements in an empty List of size ‘n’ and find the
# maximum number in the list.


n = int(input("Enter the size of the list: "))
numbers = []

for i in range(n):
    element = int(input("Enter element: "))
    numbers.append(element)

maximum = max(numbers)
print("Maximum element:", maximum)


