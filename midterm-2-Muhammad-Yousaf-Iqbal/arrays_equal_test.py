import arrays
import arrays_equal

def int_string_to_array(int_string):
    """
    Helper function that accepts a string of space separated integers
    and returns an array containing those values, e.g.
    "3 12 18 5" --> [3, 12, 18, 5]
    """
    tokens = int_string.split()
    an_array = arrays.Array(len(tokens))

    for index in range(len(tokens)):
        an_array[index] = int(tokens[index])

    return an_array

def test_empty_arrays():
    # setup
    array1 = arrays.Array(0)
    array2 = arrays.Array(0)
    expected = True

    # invoke
    actual = arrays_equal.arrays_equal(array1,array2)

    # analyze
    assert expected == actual

def test_array1_empty():
    # setup
    array1 = arrays.Array(0)
    array2 = int_string_to_array("1 2 3")
    expected = False

    # invoke
    actual = arrays_equal.arrays_equal(array1,array2)

    # analyze
    assert expected == actual

def test_array2_empty():
    # setup
    array1 = int_string_to_array("1 2 3")
    array2 = arrays.Array(0)
    expected = False

    # invoke
    actual = arrays_equal.arrays_equal(array1,array2)

    # analyze
    assert expected == actual

def test_1_element_equal():
    # setup
    array1 = int_string_to_array("1")
    array2 = int_string_to_array("1")
    expected = True

    # invoke
    actual = arrays_equal.arrays_equal(array1,array2)

    # analyze
    assert expected == actual

def test_1_element_not_equal():
    # setup
    array1 = int_string_to_array("1")
    array2 = int_string_to_array("5")
    expected = False

    # invoke
    actual = arrays_equal.arrays_equal(array1,array2)

    # analyze
    assert expected == actual

def test_10_elements_equal():
    # setup
    array1 = int_string_to_array("3 2 1 7 9 3 0 1 99 4")
    array2 = int_string_to_array("3 2 1 7 9 3 0 1 99 4")
    expected = True

    # invoke
    actual = arrays_equal.arrays_equal(array1,array2)

    # analyze
    assert expected == actual

def test_10_elements_not_equal():
    # setup
    array1 = int_string_to_array("3 2 1 7 9 3 0 1 99 4")
    array2 = int_string_to_array("3 2 7 1 9 3 0 1 99 4") # 7,1 switched
    expected = False

    # invoke
    actual = arrays_equal.arrays_equal(array1,array2)

    # analyze
    assert expected == actual

def test_diff_array1_shorter():
    # setup
    array1 = int_string_to_array("3 2 1 7")
    array2 = int_string_to_array("3 2 1 7 9")
    expected = False

    # invoke
    actual = arrays_equal.arrays_equal(array1,array2)

    # analyze
    assert expected == actual

def test_diff_array2_shorter():
    # setup
    array1 = int_string_to_array("2 1 7 9 3")
    array2 = int_string_to_array("2 1 7 9")
    expected = False

    # invoke
    actual = arrays_equal.arrays_equal(array1,array2)

    # analyze
    assert expected == actual

#Done