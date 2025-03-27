from problem_3 import *
from testing_utils import run_a_test

def test_problem_3_1():
    run_a_test(item_buffer, [], [])

def test_problem_3_2():
    run_a_test(item_buffer, [1,3,2], [1,2,3])

def test_problem_3_3():
    run_a_test(item_buffer, ['one', 'three', 'four', 'two'], ['one', 'two', 'three', 'four'])

def test_problem_3_4():
    run_a_test(item_buffer, [1, 3, 5, 6, 8, 10, 11, 13, 15, 14, 12, 9, 7, 4, 2], list(range(1,16)))

def test_problem_3_5():
    run_a_test(item_buffer, ['a', 'c', 'e', 'f', 'h', 'j', 'k', 'm', 'o', 'p', 'r', 't', 'u', 'w',\
                              'y', 'z', 'x', 'v', 's', 'q', 'n', 'l', 'i', 'g', 'd', 'b'], \
                                [chr(i) for i in range(97,123)])


