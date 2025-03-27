from unique_elements import *
def test_empty_string():
    # setup
    empty_string = ""
    expected = []
    # invoke
    actual = unique_elements(empty_string)
    # analyze
    assert expected == actual
def test_empty_set():
    # setup
    empty_set = set()
    expected = []
    # invoke
    actual = unique_elements(empty_set)
    # analyze
    assert expected == actual
def test_string():
        # setup
    a_string = "A bookkeeper keeps books"
    expected = ['A', 'r', 's', 'o', 'b', ' ', 'p', 'e', 'k']
    # invoke
    actual = unique_elements(a_string)
    # analyze
    assert sorted(expected) == sorted(actual)
def test_int_list():
        # setup
    int_list = [0, 5, 8, 9, 7, 3, 0, 5, 9, 0, 9, 6, 7, 3]
    expected = [0, 3, 5, 6, 7, 8, 9]
    # invoke
    actual = unique_elements(int_list)
    # analyze
    assert sorted(expected) == sorted(actual)
def test_boolean_tuple():
        # setup
    bool_tuple = (True, False, False, True, True, False)
    expected = [True, False]
    # invoke
    actual = unique_elements(bool_tuple)
    # analyze
    assert sorted(expected) == sorted(actual)
def test_all_unique_string():
        # setup
    a_string = "Isogram"
    expected = ["I","s","o","g","r","a","m"]
    # invoke
    actual = unique_elements(a_string)
    # analyze
    assert sorted(expected) == sorted(actual)
def test_all_same_elem_list():
        # setup
    a_list = [0,0,0,0,0,0,0]
    expected = [0]
    # invoke
    actual = unique_elements(a_list)
    # analyze
    assert expected == actual
#MYI
