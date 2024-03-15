def leap_year(year):
    if year % 4 == 0 or year % 100 != 0 and year % 400 == 0:
        print("the year is leap")
        return True
    else:
        return False


def month_days(year, month):
    month_list = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if leap_year(year) and month == 2:
        return 29
    else:
        return month_list[month - 1]


year = int(input("Enter the year "))
month = int(input("Enter the month to see days "))
days_in_month = month_days(year, month)
print(days_in_month)
