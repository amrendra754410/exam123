import math
while True:
    print("Menu:")
    print("1.Addition 2.Subtraction 3.Multiplication 4.Division 5.Exponent")
    print("6.Tan 7.Sin 8.Cos 9.Factorial 10.Log 11.Exit")
    choice=int(input("Enter your choice: "))
    if choice==11:
        print("Exiting calculator...")
        break
    if choice in [1,2,3,4,5]:
        x=float(input("Enter first number: "))
        y=float(input("Enter second number: "))
        if choice==1: result=x+y
        elif choice==2: result=x-y
        elif choice==3: result=x*y
        elif choice==4: result=x/y if y!=0 else "Division by zero error"
        elif choice==5: result=x**y
    else:
        x=float(input("Enter number: "))
        if choice==6: result=math.tan(x)
        elif choice==7: result=math.sin(x)
        elif choice==8: result=math.cos(x)
        elif choice==9: result=math.factorial(int(x))
        elif choice==10: result=math.log(x)
    print("Result:",result)
