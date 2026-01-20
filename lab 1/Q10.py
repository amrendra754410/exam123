def is_leap_year(year):
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return True
    else:
        return False

month = int(input("Enter month (1-12): "))
year = int(input("Enter year: "))

days_in_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

if month == 2 and is_leap_year(year):
    print("Number of days: 29")
else:
    print("Number of days:", days_in_month[month - 1])
