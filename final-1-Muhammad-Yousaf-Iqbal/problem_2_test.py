from problem_2 import *
from testing_utils import run_a_test

def test_problem_2_1():
    run_a_test(count_to_order, 0, [])

def test_problem_2_2():
    run_a_test(count_to_order, 1, [1])

def test_problem_2_3():
    run_a_test(count_to_order, 5, [1,2,3,4,5])

def test_problem_2_4():
    run_a_test(count_to_order, 15, [5,4,3,2,1])

def test_problem_2_5():
    run_a_test(count_to_order, 4, [3,1,2])

def test_problem_2_6():
    run_a_test(count_to_order, 55, range(10,0,-1))

