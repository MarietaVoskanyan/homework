def days(year, month):
    if year % 4 == 0 and month == 2:
        return 29
    elif year % 4 != 0 and month == 2:
        return 28
    elif month in(1, 3, 5, 7, 8, 10, 12):
        return 31
    elif month in(4, 6, 9, 11):
        return 30

year = int(input("Insert year: "))
month = int(input("Insert month: "))
print(days(year, month))
