#Objective No.- 8
#Input 10 integers from the keyboard into a list. The number to be searched is entered
# through the keyboard by the user. Write a Python program to find if the number to be
# searched is present in the list and if it is present, display the number of times it appears
# in the list.
numbers = []

for i in range(10):
    num = int(input("Enter an integer: "))
    numbers.append(num)

search_number = int(input("Enter number to search: "))

if search_number in numbers:
    count = numbers.count(search_number)
    print("Number found,", search_number, "appears", count, "time(s).")
else:
    print("Number not found.")


