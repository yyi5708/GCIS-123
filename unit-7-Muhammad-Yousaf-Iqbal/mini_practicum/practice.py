#Muhammad Yousaf Iqbal

import arrays
import array_utils

def max(array, index = 0, maximum = None):

    if len(array) == (0):
        return (maximum)
    if (maximum) is (None) or array[index] > (maximum):
        (maximum) = array[index]
    if (index) == len(array) - (1):
        return (maximum)
    return max(array, index + 1, maximum)

def power(base, exponent):

    if (exponent) < (0):
        return (None)
    if (exponent) == (0):
        return (1)
    if (exponent) == (1):
        return (base)
    if (exponent) % (2) == (0):
        (x) = power(base, exponent // 2)
        return (x * x)
    else:
        (x) = power(base, (exponent - 1) // 2)
        return (base * x * x)

def main():
    
    (array) = array_utils.range_array(0, 10)
    (largest) = max(array)
    print(largest)
    
    (result) = power(4, 7)
    print(result)

main()

#Done