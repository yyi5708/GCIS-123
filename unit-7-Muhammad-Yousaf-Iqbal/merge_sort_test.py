import merge_sort
import array_utils

def test_merge_sort():
    #setup
    an_array = array_utils.range_array(1, 1)
    #invoke
    result = merge_sort.merge_sort(an_array)
    #analyze
    for i in range(len(result)):
        assert result[i] == i