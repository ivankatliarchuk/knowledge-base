#!/usr/bin/python

def binary_search(list, item):
    low = 0
    high = len(list) - 1
    while low <= high:
        mid = (low + high)
        guess = list[mid]
        if guess == item:
            return mid
        if guess > item:
            high = mid - 1
        else:
            low = mid + 1
    return None


assert binary_search([1, 4, 77, 89, 121, 124, 789, ], 33) == None
assert binary_search([1,4,77,89,121,124,789,], 89) == 3
