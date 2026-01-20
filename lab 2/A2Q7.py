#Name- Rishit Swain
#Regd. No.- 24E119F02
#Objective No.- 7
# Write a Python program to create a list of size N and store the random values in it and fin
# d the sum and average


import random

N = int(input("Enter the size of the list: "))
numbers = []

for i in range(N):
    num = random.randint(1, 100)
    numbers.append(num)

total = sum(numbers)
average = total / N

print("List:", numbers)
print("Sum:", total)
print("Average:", average)


