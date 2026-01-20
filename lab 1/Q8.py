overtime_rate = 12.00
regular_hours = 40

for i in range(1, 11):
    print("Employee", i)
    hours_worked = float(input("Enter hours worked: "))
    
    if hours_worked > regular_hours:
        overtime_hours = hours_worked - regular_hours
        overtime_pay = overtime_hours * overtime_rate
        print("Overtime pay: Rs.", overtime_pay)
    else:
        print("No overtime pay")
