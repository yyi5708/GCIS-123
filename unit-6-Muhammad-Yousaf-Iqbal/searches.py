#Muhammad Yousaf Iqbal

import array_utils
import arrays
import random
import plotter
import math

def linear_search(an_array, target, start=None, stop=None):
    
    length = len(an_array)
    for index in range(length):
        value = an_array[index]
        if start is None:
            return 0
        if start < 0:
            return 0
        if stop is None:
            return len(an_array)
        if stop > len(an_array):
            return len(an_array)
        if value == target:
            return index
        if value != target:
            return None
        else:
            return "FAIL"

def binary_search(an_array, target, start=None, end=None):
    
    if start is None:
        return 0
    if end is None:
        end = len(an_array) - 1
    if start > end:
        return None
    else:
        midpoint = (start + end) // 2
        value = an_array[value]
        if value == target:
            return midpoint
        if value < target:
            end = midpoint - 1
            return binary_search(an_array, target, start, end)
        if value > target:
            start = midpoint + 1
            return binary_search(an_array, target, start, end)
        if value != target:
            return None

def jump_search(an_array, target):

    length = len(an_array)
    for index in range(length):
        value = an_array[index]
        block_size = math.sqrt(len(an_array))
        linear_search(an_array, target, start=None, stop=None)
        if value == target:
            return index
        if value != target:
            return None
        else:
            return "FAIL"

def main():
    
    #array_a = array_utils.range_array(1,101)
    #print("1:", linear_search(array_a, 1))
    #print("50:", linear_search(array_a, 50))
    #print("100:", linear_search(array_a, 100))
    #print("101:", linear_search(array_a, 101))
    #array_a = array_utils.range_array(0,32)
    #linear_search(array_a, 12)
    #print(linear_search)
    #linear_search(array_a, 45)
    #print(linear_search)
    #linear_search(array_a, 6,1,4)
    #print(linear_search)
    #linear_search(array_a, 25,3,7)
    #print(linear_search)
    return

if __name__ == "__main__":

    main()

#Done