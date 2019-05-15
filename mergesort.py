# Merge sort from min to max | best case n*log(n), average case n*log(n), worst case n*log(n)
import math


def merge(left, right):
    print("start merge")
    print(left, right)
    print(len(left), len(right))
    indexL = 0
    indexR = 0
    output = []
    while ((indexL < len(left)) & (indexR < len(right))):
        if (left[indexL] < right[indexR]):
            output.append(left[indexL])
            print("hitleft", left[indexL])
            indexL += 1
        else:
            output.append(right[indexR])
            print("right", right[indexR])
            indexR += 1
    print(output)
    output += left[indexL:]+right[indexR:]
    return output


def mergeSort(array):
    if len(array) == 1:
        return array
    mid = math.floor(len(array)/2)
    right = array[mid:]
    left = array[0:mid]
    print(left, right)
    return merge(mergeSort(left), mergeSort(right))


test = [9, 8, 7, 6, 5, 4, 3, 2, 1]
result = mergeSort(test)
print(result)
