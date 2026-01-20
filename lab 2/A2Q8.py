#Name- Rishit Swain
#Regd. No.- 24E119F02
#Objective No.- 8

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


