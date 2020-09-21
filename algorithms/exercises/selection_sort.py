"""Finding the s,mallest of a set of numbers"""


def findsmallest(arr:list) -> int :
    smallest = arr[0]
    smallest_index = 0
    for i in range(1, len(arr)):
        if arr[i] < smallest:
            smallest = arr[i]
            smallest_index = i
    return smallest_index

def selection_sort(arr):
    new_arr = []
    for i in range(1, len(arr)):
        number = findsmallest(arr)
        new_arr.append(arr.pop(number))
    return new_arr

print(selection_sort([5, 2, 6, 7, 10]))

