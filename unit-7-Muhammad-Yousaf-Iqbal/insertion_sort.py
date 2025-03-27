#Muhammad Yousaf Iqbal

import array_utils

def swap(an_array, a, b):
    temp = an_array[a]
    an_array[a] = an_array[b]
    an_array[b] = temp
    print(an_array)

def shift(an_array, index):
    while index > 0:
        swap(an_array, index, index-1)
        index -= 1

def insertion_sort(an_array):
    for index in range(len(an_array)):
        shift(an_array, index)

def main():
    an_array = array_utils.range_array(1, 6)
    print(an_array)
    insertion_sort(an_array)
    print(an_array)
    an_array = array_utils.range_array(10, 0, -1)
    print(an_array)
    print("\n")
    shift(an_array, 9)
    insertion_sort(an_array)
    print(an_array)

if __name__ == "__main__":
    main()

#Done