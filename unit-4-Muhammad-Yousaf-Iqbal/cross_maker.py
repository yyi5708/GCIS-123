#TOP

"""
Program for cross_maker.py that draws a crossword with user values/inputs and draw them with the turtle module.
Author: MYI.
"""

"""
Declaring global variables to use throughout the whole program.
"""

PIXEL_SIZE = (30)
ROWS = (20)
COLUMNS = (20)

"""
Importing module.
"""

import turtle

"""
Function init that delcares all the standard turtle values/actions that stay constant.
"""

#Function init.
def init():
    x = PIXEL_SIZE * COLUMNS / 2
    y = PIXEL_SIZE * ROWS / 2
    turtle.reset()
    turtle.speed(0)
    turtle.pensize(2)
    turtle.penup()
    turtle.goto(-x, y)
    turtle.pencolor("Black")
    turtle.fillcolor("White")

"""
Function move that declares which columns/rows to go to using input and turtle.
"""

#Function move.
def move(column, row):
    top_left_x = PIXEL_SIZE * COLUMNS / 2 * -1
    top_left_y = PIXEL_SIZE * ROWS / 2
    x = top_left_x + (column * PIXEL_SIZE)
    y = top_left_y + (row * PIXEL_SIZE)
    turtle.goto(x, y)

"""
Function single_letter that declares which colors to use and what letter to draw using input and turtle.
"""

#Function single_letter.
def single_letter(pen_color, fill_color, letter):
    turtle.pencolor(pen_color)
    turtle.fillcolor(fill_color)
    turtle.begin_fill()
    turtle.pendown()
    turtle.forward(30)
    turtle.left(90)
    turtle.forward(30)
    turtle.left(90)
    turtle.forward(30)
    turtle.left(90)
    turtle.forward(30)
    turtle.left(90)
    turtle.forward(15)
    turtle.write(letter, align='center', font=("Arial", 19, "normal"))
    turtle.end_fill()
    turtle.penup()

"""
Function validate that checks to make sure the requested user input of the word and direction is correct and will not crash the program. Checks to see if the word is too long for the grid and if the direction is correctly stated.
"""

#Function validate.
def validate(x, y, word, direction):
    grid_rows = ROWS
    grid_columns = COLUMNS
    word_length = len(word)
    if direction == "horizontal" or "h":
        if y + word_length > grid_columns:
            print("Error: The word does not fit within the grid columns.")
            return False
        return True
    if direction == "vertical" or "v":
        if x + word_length > grid_rows:
            print("Error: The word does not fit within the grid rows.")
            return False
        return True
    else:
        print("Error: You entered an invalid direction, use either 'horizontal' / 'h' or 'vertical' / 'v'.")
        return False

"""
Function write_word that again uses the same parameters as the validate function but this time writes the word/letter after it has passed the verification process. I had some issues with this part of the program/function and did not know what to do...
"""

#Function write_word.
def write_word(x, y, word, direction):
    if validate(x, y, direction, word):
        word_length = len(word)
        if direction == "horizontal" or "h":
            for i in range(word_length):
                [x] = word[i]
        if direction == "vertical" or "v":
            for i in range(word_length):
                [y] = word[i]
        else:
            print("Error: You entered an invalid direction, use either 'horizontal' / 'h' or 'vertical' / 'v'.")
            return False
    else:
        return False

"""
Function main that runs/executes all programs/functions.
"""

#Function main.
def main():
    turtle.screensize(canvwidth=20, canvheight=20, bg="White")
    init()
    #validate(5, -5, "CROSSWORDS", "horizontal")
    #write_word(5, -5, "CROSSWORDS", "horizontal")
    move(5, -5)
    single_letter("Black", "Yellow", "C")
    move(6,-5)
    single_letter("Black", "Yellow", "R")    
    move(7,-5)
    single_letter("Black", "Yellow", "O")
    move(8,-5)
    single_letter("Black", "Yellow", "S")
    move(9,-5)
    single_letter("Black", "Yellow", "S")
    move(10,-5)
    single_letter("Black", "Yellow", "W")
    move(11, -5)
    single_letter("Black", "Yellow", "O")
    move(12,-5)
    single_letter("Black", "Yellow", "R")    
    move(13,-5)
    single_letter("Black", "Yellow", "D")
    move(14,-5)
    single_letter("Black", "Yellow", "S")
    #validate(6, -4, "AE", "vertical")
    #write_word(6, -4, "AE", "vertical")
    move(6,-4)
    single_letter("Black", "Yellow", "A")
    move(6,-6)
    single_letter("Black", "Yellow", "E")
    #validate(11, -4, "FR", "vertical")
    #write_word(11, -4, "FR", "vertical")
    move(11,-4)
    single_letter("Black", "Yellow", "F")
    move(11,-6)
    single_letter("Black", "Yellow", "R")
    #validate(14, -1, "NERD", "vertical")
    #write_word(14, -1, "NERD", "vertical")
    move(14,-1)
    single_letter("Black", "Yellow", "N")
    move(14,-2)
    single_letter("Black", "Yellow", "E")
    move(14,-3)
    single_letter("Black", "Yellow", "R")
    move(14,-4)
    single_letter("Black", "Yellow", "D")
    turtle.hideturtle()
    input("Press enter to exit: ")

#Special line for main to make sure the test files run correctly without crashing.
if __name__== "__main__":
    #Deploys main function.
    main()

#BOTTOM