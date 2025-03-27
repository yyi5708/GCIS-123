#Muhammad Yousaf Iqbal

import array_utils
import arrays
import plotter
import searches

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

def sort_col(filepath, i_col, size):
    try:
        with open(filepath) as file:
            next(file)
            col_size = arrays.Array(size)
            i = 0
            for line in file:
                col_value = line.strip() and line.split(",")
                col_size[i] = int(col_value[i_col])
                i += 1
            an_array = col_size
            print(col_size)
            print("\n")
            shift(col_size, size)
            insertion_sort(an_array)
            print(an_array)
    except:
        print(FileNotFoundError) or print(ValueError) or print(IndexError)

def insertion_sort_backwards(an_array):
    for index in range(len(an_array)-1, -1, -1):
        shift_backwards(an_array, index)
        print(an_array)

def shift_backwards(an_array, index):
    while index < len(an_array)-1:
        if an_array[index] > an_array[index+1]:
            swap(an_array, index, index+1)
            index += 1
        else:
            break

def main():
    sort_col("./data/dataset.csv", 2, 189)
    print("\n")
    sort_col("./data/dataset.csv", 7, 189)
    an_array = [5, 3, 7, 4, 1]
    insertion_sort_backwards(an_array)

if __name__ == '__main__':
    main()

#Done