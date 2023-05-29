def isLeap(year):
    if year % 4 != 0:
        return 0
    elif year % 100 == 0 and year % 400 != 0:
        return 0
    else:
        return 1