def insertionSort(list):
    for i in range(len(list)):
        j = i
        while j > 0 and list[j-1] > list[j]:
            list[j], list[j-1] = list[j-1], list[j]
            j = j - 1
    return list

print(insertionSort([9,1,3,4,2,7,5,3,6,9,8,0,2,1,7,6,5,4,8,0]))