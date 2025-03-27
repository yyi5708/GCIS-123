#Muhammad Yousaf Iqbal


import searches
import array_utils
import arrays
import random
import plotter
import math

def test_binary_search_start_greater():
    
    an_array = None
    target = None
    expected =  0
    start = None
    end = None
    actual = searches.binary_search(an_array, target, start, end)
    assert expected == actual

def test_binary_search_midpoint():

    an_array = array_utils.range_array(0,101)
    target = 50
    expected = 0
    actual = searches.binary_search(an_array, target)
    assert expected == actual

def test_binary_search_left():

    an_array = array_utils.range_array(0,101)
    target = 24
    expected = 0
    actual = searches.binary_search(an_array, target)
    assert expected == actual

def test_binary_search_right():

    an_array = array_utils.range_array(0,101)
    target = 75
    expected = 0
    actual = searches.binary_search(an_array, target)
    assert expected == actual

def test_binary_search_five():
    
    an_array = array_utils.range_array(0,101)
    target = 5
    expected = 0
    actual = searches.binary_search(an_array, target)
    assert expected == actual

def test_linear_search_five():

    an_array = array_utils.range_array(0,101)
    target = 5
    expected = 0
    actual = searches.binary_search(an_array, target)
    assert expected == actual

def test_linear_search_correct():
    
    an_array = array_utils.range_array(0,101)
    target = 10
    expected = 0
    actual = searches.linear_search(an_array, target)
    assert expected == actual

def test_linear_search_incorrect():
    
    an_array = array_utils.range_array(0,101)
    target = 10
    expected = 0
    actual = searches.linear_search(an_array, target)
    assert expected == actual

#Done