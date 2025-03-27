import arrays
import array_utils

def merge_sort(an_array):
    if len(an_array) < 2:
        return an_array
    
def split(an_array):
    evens_count = (len(an_array) + 1) // 2
    odds_count = len(an_array) // 2
    evens = arrays.Array(evens_count)
    odds = arrays.Array(odds_count)
    isEven = True
    for i in range (len(an_array)):
        if isEven:
            evens[i // 2] = an_array[i]
        else:
            odds[i // 2] = an_array[i]
        isEven = not isEven
    return (evens, odds)

def main():
    an_array = array_utils.range_array(0, 10, 1)
    print(an_array)
    x, y = split(an_array)
    print(x)
    print(y)

main()