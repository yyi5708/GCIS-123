import arrays
import random

def range_array(start, stop, step=1):
    a_range = range(start, stop, step)
    length = len(a_range)
    an_array = arrays.Array(length, 0)
    for index in range(length):
        an_array[index] = a_range[index]
    return an_array

def random_array(size, min_value=0, max_value=None):
    an_array = arrays.Array(size, 0)
    if max_value is None:
        max_value = size

    for index in range(size):
        an_array[index] = random.randint(min_value, max_value)
    
    return an_array

def random_sorted_array(size, min_value = 0, max_diff = None):
    an_array = arrays.Array(size)
    value = min_value
    if max_diff == None:
        max_diff = 4
    for i in range(size):
        next_diff = random.randint(1, max_diff)
        value += next_diff
        an_array[i] = value
    return an_array

def copy_array(an_array, length=None):
    if length == None:
        length = len(an_array)
    copy = arrays.Array(length)
    print(len(copy))
    for i in range(length):
        copy[i] = an_array[i]
    return copy