import quicksort
import array_utils

def test_quick_sort():
    #setup
    an_array = array_utils.range_array(1, 1)
    #invoke
    result = quicksort.merge_sort(an_array)
    #analyze
    for i in range(len(result)):
        assert result[i] == i