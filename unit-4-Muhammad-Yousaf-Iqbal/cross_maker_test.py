#TOP

"""
Program that checks/tests functions for verifying the assertle, init, move, single_letter, validate, write_word, have the correct input/output for the cross_maker module/file.
Program for testing all functions from cross_maker.py
Author: MYI.
"""

"""
Declaring global variables to use throughout the whole program.
"""

PIXEL_SIZE = (30)
ROWS = (20)
COLUMNS = (20)

"""
Importing modules.
"""

import turtle
import cross_maker

"""
Function assertle_1 that declares constants for turtle/throughout the program. Testing to make sure everything works correctly as expected.
"""

#Function assertle_1.
def assertle_1(pen_color, fill_color):
    assert turtle.speed() == 0
    assert turtle.pensize() == 2
    assert turtle.xcor() == 0
    assert turtle.ycor() == 0
    assert turtle.isdown() == False
    assert turtle.pencolor() == pen_color
    assert turtle.fillcolor() == fill_color

"""
Function assertle_2 that declares constants for turtle/throughout the program. Testing to make sure everything works correctly as expected.
"""

#Function assertle_2.
def assertle_2(column, row):
    assert turtle.speed() == 0
    assert turtle.xcor() == column
    assert turtle.ycor() == row
    assert turtle.isdown() == False

"""
Function assertle_3 that declares constants for turtle/throughout the program. Testing to make sure everything works correctly as expected.
"""

#Function assertle_3.
def assertle_3(pen_color,fill_color):
    assert pen_color == "Black"
    assert fill_color == "Yellow"

"""
Function test_init that tests the whole init function.
"""

#Function test_init.
def test_init():
    #setup
    cross_maker.init()
    #invoke
    cross_maker.init()
    #analyze
    assertle_1("Black", "White")

"""
Function test_move that tests the whole move function.
"""

#Function test_move.
def test_move():
    #setup
    COLUMNS = 20
    ROWS = 20
    #invoke
    cross_maker.move(COLUMNS,ROWS)
    #analyze
    assertle_2(0, 0)

"""
Function test_single_letter that tests the whole single_letter function.
"""

#Function test_single_letter.
def test_single_letter():
    #setup
    cross_maker.init()
    #invoke
    cross_maker.single_letter("Black", "Yellow", "W")
    #analyze
    assertle_3("Black", "Yellow")

"""
Function test_validate that tests the whole validate function.
"""

#Function test_validate.
def test_validate():
    #setup
    x = 0
    y = 0
    word = "crosswordsarefornerds"
    direction = "horizontal"
    expected = False
    #invoke
    actual = cross_maker.validate(x, y, word, direction)
    #analyze
    assert expected == actual

"""
Function test_write_word that tests the whole write_word function.
"""

#Function write_word.
def test_write_word():
    #setup
    x = 0
    y = 0
    word = "crosswords"
    direction = "straight"
    expected = None
    #invoke
    actual = cross_maker.write_word(x, y, word, direction)
    #analyze
    assert expected == actual

#BOTTOM