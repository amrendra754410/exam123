def gcd(a, b):
    while b != 0:
        temp = b
        b = a % b
        a = temp
    return a

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

result = gcd(num1, num2)
print("GCD of", num1, "and", num2, "is", result)


