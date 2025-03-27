#TOP

"""
Program that checks/tests functions for verifying the single/multiple colors have the correct input/output for the get_color function that has all the strings, indexes, comma-seperated-values, etc.
Program for testing the function get_color from turtlecraft.py.
Author: MYI.
"""

"""
Importing module.
"""

import turtlecraft

"""
Function to test single colors.
"""

#Function test_single_color.
def test_single_color():
    #setup
    answer = [0]
    guess = [0]
    expected = ("red")
    #invoke
    actual = turtlecraft.get_color()
    #analyze
    assert expected == actual

"""
Function to test multiple colors.
"""

#Function test_multiple_color.
def test_multiple_color():
    #setup
    answer = 0 and 4
    guess = 0 and 4
    expected = ("red,blue")
    #invoke
    actual = turtlecraft.get_color()
    #analyze
    assert expected == actual

#BOTTOM