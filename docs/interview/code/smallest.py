#!/usr/bin/python

def find_smallest(a):
    return min(set(a))


assert find_smallest([189, 4, 77, 89, 121, 2, 124, 789,]) == 2
assert find_smallest([1, 4, 77, 89, 121, 124, 789, -2]) == -2
