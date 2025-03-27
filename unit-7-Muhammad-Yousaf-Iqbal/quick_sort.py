#Muhammad Yousaf Iqbal

import arrays
import array_utils

def quicksort(pivot, an_array):
    if len(an_array) < 2:
        return an_array
    else:
        less = arrays.Array(len(an_array))
        same = arrays.Array(len(an_array))
        more = arrays.Array(len(an_array))
        less_index = 0
        same_index = 0
        more_index = 0
        for i in range (len(an_array)):
            if an_array[i] < pivot:
                less [less_index] = an_array[i]
                less_index += 1
            if an_array[i] > pivot:
                more [more_index] = an_array[i]
                more_index += 1
            if an_array[i] == pivot:
                same [same_index] = an_array[i]
                same_index += 1
        return array_utils.copy_array(less, less_index), array_utils.copy_array(same, same_index), array_utils.copy_array(more, more_index)

def quick_insertion_sort(pivot, an_array):
    if (len(an_array) < 2):
        return (an_array)
    if (len(an_array) <= 20):
        for i in range(len(an_array)):
            (base) = (an_array[i])
            (x) = (i - 1)
            (y) = (x + 1)
            while (x >= 0) and (an_array[x] > base):
                (an_array[y]) = (an_array[x])
                (x) -= (1)
            (an_array[y]) = (base)
        return an_array
    else:
        less = arrays.Array(len(an_array))
        same = arrays.Array(len(an_array))
        more = arrays.Array(len(an_array))
        less_index = 0
        same_index = 0
        more_index = 0
        for i in range (len(an_array)):
            if an_array[i] < pivot:
                less [less_index] = an_array[i]
                less_index += 1
            if an_array[i] > pivot:
                more [more_index] = an_array[i]
                more_index += 1
            if an_array[i] == pivot:
                same [same_index] = an_array[i]
                same_index += 1
        return array_utils.copy_array(less, less_index), array_utils.copy_array(same, same_index), array_utils.copy_array(more, more_index)

def main():

    #unsorted = array_utils.random_array(2)
    #print("Unsorted Array: ", unsorted)
    #sorted = quicksort(1, unsorted)
    #print("Sorted Array: ", sorted)
    #unsorted = array_utils.random_array(20)
    #print("Unsorted Array: ", unsorted)
    #sorted = quicksort(10, unsorted)
    #print("Sorted Array: ", sorted)
    #unsorted = array_utils.random_array(2)
    #print("Unsorted Array: ", unsorted)
    #sorted = quick_insertion_sort(1, unsorted)
    #print("Sorted Array: ", sorted)
    #unsorted = array_utils.random_array(20)
    #print("Unsorted Array: ", unsorted)
    #sorted = quick_insertion_sort(10, unsorted)
    #print("Sorted Array: ", sorted)
    #unsorted = array_utils.random_array(200)
    #print("Unsorted Array: ", unsorted)
    #sorted = quick_insertion_sort(100, unsorted)
    #print("Sorted Array: ", sorted)
    return

if __name__ == "__main__":
    main()

#Done