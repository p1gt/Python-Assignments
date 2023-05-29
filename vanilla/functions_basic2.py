def countdown(n):
    list = []
    for i in range (n, -1, -1):
        list.append(i)
    return list
print(countdown(10))

def printAndReturn(list):
    print(list[0])
    return list[1]
print(printAndReturn([0,1]))

def firstPlusLength(list):
    return list[0] + len(list)
print(firstPlusLength([5,4,3,2,1,0]))

def valuesGreaterThanSecond(list):
    count = 0
    newList = []
    for i in range(len(list)):
        if len(list) < 2:
            return False
        elif list[i] > list[1]:
            count += 1
            newList.append(list[i])
    print(count)
    return newList
print(valuesGreaterThanSecond([5,2,3,2,1,4]))
print(valuesGreaterThanSecond([3]))

def thisLengthThatValue(size,value):
    list = []
    for i in range(size):
        list.append(value)
    return list
print(thisLengthThatValue(4,7))
print(thisLengthThatValue(6,2))