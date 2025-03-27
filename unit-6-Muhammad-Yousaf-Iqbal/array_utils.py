import arrays
import random

def random_array(size, min_value=0, max_value=None):
    an_array = arrays.Array(size, 0)
    if max_value is None:
        max_value == size
    for index in range(size):
            an_array[index] = random.randint(min_value, max_value)
    return an_array

def range_array(start, stop, step=1):
    x = range(start, stop, step)
    y = arrays.Array(x)
    for index in range[x]:
        return (y[index])

def main():
    #x = random_array(10)
    #print(x)
    x = range_array(0, 10, 1)
    y = range_array(0, 15, 1)
    z = range_array(0, 20, 1)
    print(x)
    print(y)
    print(z)

main()
