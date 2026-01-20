days_late = int(input("Enter number of days late: "))

if days_late <= 0:
    print("No fine. Book returned on time")
elif days_late <= 5:
    fine = days_late * 0.50
    print("Fine: Rs.", fine)
elif days_late <= 10:
    fine = (5 * 0.50) + ((days_late - 5) * 1.00)
    print("Fine: Rs.", fine)
elif days_late <= 30:
    fine = (5 * 0.50) + (5 * 1.00) + ((days_late - 10) * 5.00)
    print("Fine: Rs.", fine)
else:
    print("Membership cancelled due to late return")



