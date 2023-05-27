def isLeapYear(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return 1
            else:
                return 0
        else:
            return 1
    else:
        return 0
print(isLeapYear(2024))
print(isLeapYear(1992))
print(isLeapYear(1700))
print(isLeapYear(1600))
print(isLeapYear(2002))
print(isLeapYear(-5))
