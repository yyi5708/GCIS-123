"""
Various useful array utilities. Provided for use on the homework in this unit.

@author GCCIS Faculty and Muhammad Yousaf Iqbal
"""

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

def copy_array(an_array, length = None):
    if length == None:
        length = len(an_array)
    copy = arrays.Array(length)
    for i in range(length):
        copy[i] = an_array[i]
    return copy

def cat_array(a1, a2):
    result = arrays.Array(len(a1)+len(a2))
    for i in range(len(a1)):
        result[i] = a1[i]
    for i in range(len(a1), len(result)):
        result[i] = a2[i-len(a1)]
    return result

def increasing_comparator(a, b):
    if b>= a:
        return True
    else:
        return False

def decreasing_comparator(a, b):
    if b <= a:
        return True
    else:
        return False

def is_sorted(an_array, comparator=increasing_comparator):
    if an_array is comparator:
        return True
    if an_array is not comparator:
        return False
    if an_array == comparator:
        return True
    if an_array != comparator:
        return False
    else:
        return False

def main():
    #random.seed(1)
    #rand_array = random_array(10)
    #print(rand_array)
    array1 = [20, 10, 30]
    a = is_sorted(array1)
    print(a)
    b = is_sorted(array1, decreasing_comparator)
    print(b)
    array2 = [30, 20, 10]
    c = is_sorted(array2, increasing_comparator)
    print(c)
    d = is_sorted(array2, decreasing_comparator)
    print(d)

if __name__ == "__main__":
    main()

#Done