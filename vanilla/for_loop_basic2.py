def biggieSize(list):
    for i in range(len(list)):
        if list[i] > 0:
            list[i] = "big"
    return list
print(biggieSize([-1, 3, 5, -5]))

def countPositives(list):
    count = 0
    for i in range(len(list)):
        if list[i] > 0:
            count += 1
    list.pop()
    list.append(count)
    return list
print(countPositives([-1,1,1,1]))
print(countPositives([1,6,-4,-2,-7,-2]))

def sumTotal(list):
    sum = 0
    for i in range(len(list)):
        sum += list[i]
    return sum
print(sumTotal([1,2,3,4]))
print(sumTotal([6,3,-2]))

def average(list):
    sum = 0
    for i in range(len(list)):
        sum += list[i]
    return sum/len(list)
print(average([1,2,3,4]))

def length(list):
    return len(list)
print(length([37,2,1,-9]))
print(length([]))

def minimum(list):
    min = list[0]
    for i in range(len(list)):
        if min > list[i]:
            min = list[i]
    return min
print(minimum([37,2,1,-9]))

def maximum(list):
    max = list[0]
    for i in range(len(list)):
        if max < list[i]:
            max = list[i]
    return max
print(maximum([37,2,1,-9]))

def ultimateAnalysis(list):
    UA = {
        'sumTotal': sumTotal(list),
        'average': average(list),
        'minimum': minimum(list),
        'maximum': maximum(list),
        'length': length(list)
    }
    return UA
print(ultimateAnalysis([37,2,1,-9]))

def reverse(list):
    length = len(list)
    mid = length // 2
    for i in range(mid):
        list[i], list[length - i - 1] = list[length - i - 1], list[i]
    return list
print(reverse([37,2,1,-9]))