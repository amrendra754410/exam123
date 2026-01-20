n = int(input("Enter the number of terms: "))

first = 0
second = 1
count = 0

if n <= 0:
    print("Enter a positive integer")
elif n == 1:
    print(first)
else:
    while count < n:
        print(first)
        temp = first + second
        first = second
        second = temp
        count += 1


