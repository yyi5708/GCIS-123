from ascii_tuples import *
def test_sort_ascii_tuples_empty():
    # setup
    ascii_tuple_list = []
    expected = []
    # invoke
    actual = sort_ascii_tuples(ascii_tuple_list)
    # analyze
    assert expected == actual
def test_sort_ascii_tuples_1_element():
    # setup
    ascii_tuple_list = [(114, 97, 98, 98, 105, 116)]
    expected = [(114, 97, 98, 98, 105, 116)]
    # invoke
    actual = sort_ascii_tuples(ascii_tuple_list)
    # analyze
    assert expected == actual
def test_sort_ascii_tuples_many_elements():
    # setup
    ascii_tuple_list = [(100, 111, 103), (99, 97, 114), (105, 116),
                        (99, 97, 107, 101), (104, 111, 117, 115, 101), (97,),
                        (115, 104, 97, 114, 107), (98, 117, 115),
                        (99, 114, 111, 99, 111, 100, 105, 108, 101)]
    expected = [(97,), (105, 116), (99, 97, 114), (100, 111, 103),
                (98, 117, 115), (99, 97, 107, 101), (115, 104, 97, 114, 107),
                (104, 111, 117, 115, 101),
                (99, 114, 111, 99, 111, 100, 105, 108, 101)]
    # invoke
    actual = sort_ascii_tuples(ascii_tuple_list)
    # analyze
    assert expected == actual
def test_make_ascii_tuples_empty():
    # setup
    word_list = []
    expected = []
    # invoke
    actual = make_ascii_tuples(word_list)
    # analyze
    assert expected == actual
def test_make_ascii_tuples_1_element():
    # setup
    word_list = ["rabbit"]
    expected = [(114, 97, 98, 98, 105, 116)]
    # invoke
    actual = make_ascii_tuples(word_list)
    # analyze
    assert expected == actual
def test_make_ascii_tuples_many_elements():
    # setup
    word_list = ["dog","car","it","cake","house","a","shark","bus","crocodile"]
    expected = [(100, 111, 103), (99, 97, 114), (105, 116), (99, 97, 107, 101),
                (104, 111, 117, 115, 101), (97,), (115, 104, 97, 114, 107),
                (98, 117, 115), (99, 114, 111, 99, 111, 100, 105, 108, 101)]
    # invoke
    actual = make_ascii_tuples(word_list)
    # analyze
    assert expected == actual
#MYI
