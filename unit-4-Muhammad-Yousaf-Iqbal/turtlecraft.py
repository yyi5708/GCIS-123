#TOP

"""
Program for turtlecraft.py that draws pixel art with user values/inputs and draws them with the turtle module.
Author: MYI.
"""

"""
Importing module.
"""

import turtle

"""
Declaring global variables to use throughout the whole program.
"""

PIXEL_SIZE = (32)
ROWS = (16)
COLUMNS = (16)

"""
Function for given a comma seperated string of colors and a starting index will return the characters from the starting index until the next comma or end of the string.
"""

#Function get_color.
def get_color(x):
    string = "red,blue,green,yellow"
    x = input()
    red = string[0:3]
    if x == (0,1,2,3):
        print(red)
    blue = string[4:8]
    if x == (4,5,6,7,8):
        print(blue)
    green = string[9:14]
    if x == (9,10,11,12,13,14):
        print(green)
    yellow = string[15:21]
    if x == string[15,16,17,18,19,20,21]:
        print(yellow)
    else:
        return None

"""
Function init that delcares all the standard turtle values/actions that stay constant.
"""

#Function init.
def init():
    x = PIXEL_SIZE * COLUMNS / 2
    y = PIXEL_SIZE * ROWS / 2
    turtle.reset()
    turtle.speed(0)
    turtle.up()
    turtle.goto(-x, y)
    turtle.pencolor("Black")
    turtle.fillcolor("White")

"""
Function that draws a single pixel with the user input of the color and uses the turtle module to draw it.
"""

#Function pixel.
def pixel(pixel_color):
    turtle.pencolor("Black")
    turtle.fillcolor(pixel_color)
    turtle.begin_fill()
    turtle.down()
    turns = 4
    while turns != 0:
        turtle.forward(PIXEL_SIZE)
        turtle.right(90)
        turns = turns - 1
    turtle.end_fill()
    turtle.up()
    turtle.forward(PIXEL_SIZE)

"""
Function move that uses user input of what column and row to go to so it can be ready to draw the next set of pixels the user enters.
"""

#Function move.
def move(column, row):
    top_left_x = PIXEL_SIZE * COLUMNS / 2
    top_left_y = PIXEL_SIZE * ROWS / 2
    x = top_left_x + (column * PIXEL_SIZE)
    y = top_left_y + (row * PIXEL_SIZE)
    turtle.goto(x, y)

"""
Function colors that draws an entire turtlecraft block with the pixel function using different colors.
"""

#Function colors.
def colors():
    pixel("red")
    pixel("blue")
    pixel("green")
    pixel("yellow")
    pixel("red")
    pixel("blue")
    pixel("green")
    pixel("yellow")
    pixel("red")
    pixel("blue")
    pixel("green")
    pixel("yellow")
    pixel("red")
    pixel("blue")
    pixel("green")
    pixel("yellow")

"""
Function "main" that runs/executes all programs/functions. 
"""

#Function main.
def main():
    #x = input("Enter a number from 0-20: ")
    #get_color(x)
    turtle.speed(0)
    init()
    colors()
    turtle.goto(-256,223)
    colors()
    turtle.goto(-256,190)
    colors()
    turtle.goto(-256,157)
    colors()
    turtle.goto(-256,124)
    colors()
    turtle.goto(-256,91)
    colors()
    turtle.goto(-256,58)
    colors()
    turtle.goto(-256,25)
    colors()
    turtle.goto(-256,-8)
    colors()
    turtle.goto(-256,-41)
    colors()
    turtle.goto(-256,-74)
    colors()
    turtle.goto(-256,-107)
    colors()
    turtle.goto(-256,-140)
    colors()
    turtle.goto(-256,-173)
    colors()
    turtle.goto(-256,-206)
    colors()
    turtle.goto(-256,-239)
    colors()
    turtle.hideturtle()
    input("Press enter to exit: ")

#Special line for main to make sure the test files run correctly without crashing.
if __name__== "__main__":
    #Deploys main function.
    main()

#BOTTOM