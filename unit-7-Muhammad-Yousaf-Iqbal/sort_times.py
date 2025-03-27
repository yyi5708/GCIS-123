#Muhammad Yousaf Iqbal

import time
import array_utils
import plotter
import random
import insertion_sort
import merge_sort
import quick_sort

SIZES = [200, 500, 800, 1100, 1400, 1700, 2000]

def insertion_sort_function_timer(an_array):
    start = time.perf_counter()
    insertion_sort.insertion_sort(an_array)
    stop = time.perf_counter()
    elapsed = stop - start
    return elapsed

def sort_function_timer(an_array, sort_function):
    start = time.perf_counter()
    sort_function(an_array)
    stop = time.perf_counter()
    elapsed = stop - start
    return elapsed

def plot_sort_time_using_random_arrays(sort_function):
    plotter.new_series()
    for x in SIZES:
        array = [random.randint(1, x) for i in range(x)]
        time = sort_function_timer(sort_function, array)
        plotter.add_data_point(x)
        return time

def plot_sort_time_using_sorted_arrays(sort_function):
    plotter.new_series()
    for x in SIZES:
        array = [array_utils.random_sorted_array(x, 1) for i in range(x)]
        time = sort_function_timer(sort_function, array)
        plotter.add_data_point(x)
        return time

def main():
    #sorted_array = array_utils.range_array(0, 10)
    #print("Insertion sort for sorted array: ")
    #print(sort_function_timer(sorted_array, sorts.insertion_sort))
    #plotter.init("Insertion Sort, Merge Sort, and Quick Sort", "Array Size", "Time")
    #plot_sort_time_using_random_arrays(insertion_sort.insertion_sort(SIZES))
    #plot_sort_time_using_random_arrays(merge_sort.split(SIZES))
    #plot_sort_time_using_random_arrays(quick_sort.quicksort(5, SIZES))
    #plotter.plot()
    #input("EXIT: ")
    #plotter.init("Insertion Sort, Merge Sort, and Quick Sort", "Array Size", "Time")
    #plot_sort_time_using_sorted_arrays(insertion_sort.insertion_sort(SIZES))
    #plot_sort_time_using_sorted_arrays(merge_sort.split(SIZES))
    #plot_sort_time_using_sorted_arrays(quick_sort.quicksort(5, SIZES))
    #plotter.plot()
    #input("EXIT: ")    
    return

if __name__ == "__main__":
    main()

#Done