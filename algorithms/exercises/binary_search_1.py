"""Implementing binary search"""


def binary_search(element_list: list, item: int) -> int:
    """if item in element list return the position,
    else return None"""
    low = 0
    high = len(element_list) - 1
    while low <= high:
        mid = (low + high)
        print(f'mid {mid}')
        guess = element_list[mid]
        print(f'guess {guess}')
        if guess == item:
            return mid
        if guess > item:
            high = mid - 1
            print(f'high {high}')
        else:
            low = mid + 1
            print(f'low {low}')
    return None


ELEMENT = [1, 3, 5, 7, 9]
print(binary_search(ELEMENT, 3))  # => 1
#print(binary_search(ELEMENT, -1))  # => None
