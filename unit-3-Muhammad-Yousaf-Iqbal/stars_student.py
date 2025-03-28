#START

"""
Program that draws a sky filled with stars and planets at random places. The code initially had many problems and errors and would not run but with some modifications and tweaks, the programs works perfectly now and runs as expected producing the correct drawing.
@author: MYI
"""

import random
import turtle

def tweak(speed, tracer):
    """
    Adjust the turtle's speed and tracer settings so that it can be sped up
    or slowed down as needed for visual debugging.
    """
    turtle.speed(speed)
    turtle.tracer(tracer)

def random_yellow():
    """
    Sets the turtle's fill color to a random shade of yellow using RGB values.
    """
    # the random.random() function returns a floating point value between
    # 0.1 and 1.0. This expression guarantees that the red value will be
    # between 0.5 and 1.0.
    red = 0.5 + random.random() * 0.5
    green = red
    blue = red / 2
    # the turtle color can be set using RGB values ranging from 0.0 to 1.0. In
    # this case the red and green values are between 0.5 and 1.0 and the blue
    # value is half the value - this guarantees a shade of yellow.
    turtle.color(red, green, blue)
    """Dont know the type of error but the fillcolor was set to red blue green, but it should have been red green blue...seems like a name error or type error idk but it was just mismatched...noticed this error because all my stars were a purple/pink color lol. Or maybe its an semantic error because it doesnt give the correct results."""
    turtle.fillcolor(red, green, blue)

def random_move():
    """
    Moves the turtle to a random location and orientation on the screen.
    """
    x = random.randint(-1000, 1000)
    """Syntax Error, Missing "," after the 1st number to seperate both values, VS Code highlighted the problem and/or running the program crashed with a syntax error, It showed up in the problems tab and thats how I found it and fixed it."""
    y = random.randint(-1000, 1000)
    """Name Error, Wrong Variable Called, should be "y" not "x", It showed up in terminal and I quickly fixed it by looking a few lines up and saw that x and y were created but only x was twice, it should be once x and y."""
    turtle.goto(x, y)
    angle = random.randint(0, 360)
    """Syntax Error, Missing ":" after function definition, VS Code highlighted the problem and/or running the program crashed with a syntax error, It showed up in the problems tab and thats how I found it and fixed it."""

def draw_star(length):
    """
    Draws a star at the turtle's current location and orientation.
    """
    random_yellow()
    length = random.randint(5, 10)
    turtle.pendown()
    turtle.begin_fill()
    turtle.forward(length)
    turtle.left(36)
    turtle.forward(length)
    turtle.right(108)
    turtle.forward(length)
    turtle.left(36)
    turtle.forward(length)
    turtle.right(108)
    turtle.forward(length)
    turtle.left(36)
    turtle.forward(length)
    turtle.right(108)
    turtle.forward(length)
    turtle.left(36)
    turtle.forward(length)
    turtle.right(108)
    turtle.forward(length)
    turtle.left(36)
    turtle.forward(length)
    turtle.right(108)
    turtle.end_fill()
    turtle.penup()   

def random_star(length):
    """
    Draws a random star at a random location.
    """
    random_move()
    draw_star(length)

def draw_world(x, y, radius, fill_color):
    """
    Draws planets/worlds around the screen at the desired point.
    """
    turtle.goto(x, y)
    turtle.pendown()
    turtle.fillcolor(fill_color)
    turtle.begin_fill()
    turtle.circle(radius)
    turtle.end_fill()
    turtle.penup()

def draw_celestial_bodies(length):
    """
    Draws atleast 100 stars at varios different locations and sizes and also draws the planets/worlds as well.
    """
    random_star(length)
    random_star(length)
    random_star(length)
    random_star(length)
    random_star(length)
    random_star(length)
    random_star(length)
    random_star(length)
    random_star(length)
    random_star(length)
    random_star(length)
    random_star(length)
    random_star(length)
    random_star(length)
    random_star(length)
    random_star(length)
    random_star(length)
    random_star(length)
    random_star(length)
    random_star(length)
    random_star(length)
    random_star(length)
    random_star(length)
    random_star(length)
    random_star(length)
    random_star(length)
    random_star(length)
    random_star(length)
    random_star(length)
    random_star(length)
    random_star(length)
    random_star(length)
    random_star(length)
    random_star(length)
    random_star(length)
    random_star(length)
    random_star(length)
    random_star(length)
    random_star(length)
    random_star(length)
    random_star(length)
    random_star(length)
    random_star(length)
    random_star(length)
    random_star(length)
    random_star(length)
    random_star(length)
    random_star(length)
    random_star(length)
    random_star(length)
    random_star(length)
    random_star(length)
    random_star(length)
    random_star(length)
    random_star(length)
    random_star(length)
    random_star(length)
    random_star(length)
    random_star(length)
    random_star(length)
    random_star(length)
    random_star(length)
    random_star(length)
    random_star(length)
    random_star(length)
    random_star(length)
    random_star(length)
    random_star(length)
    random_star(length)
    random_star(length)
    random_star(length)
    random_star(length)
    random_star(length)
    random_star(length)
    random_star(length)
    random_star(length)
    random_star(length)
    random_star(length)
    random_star(length)
    random_star(length)
    random_star(length)
    random_star(length)
    random_star(length)
    random_star(length)
    random_star(length)
    random_star(length)
    random_star(length)
    random_star(length)
    random_star(length)
    random_star(length)
    random_star(length)
    random_star(length)
    random_star(length)
    random_star(length)
    random_star(length)
    random_star(length)
    random_star(length)
    random_star(length)
    random_star(length)
    random_star(length)
    random_star(length)
    random_star(length)
    random_star(length)
    random_star(length)
    random_star(length)
    random_star(length)
    random_star(length)
    random_star(length)
    random_star(length)
    random_star(length)
    random_star(length)
    random_star(length)
    random_star(length)
    random_star(length)
    random_star(length)
    random_star(length)
    random_star(length)
    random_star(length)
    random_star(length)
    random_star(length)
    random_star(length)
    random_star(length)
    random_star(length)
    random_star(length)
    random_star(length)
    random_star(length)
    random_star(length)
    random_star(length)
    random_star(length)
    random_star(length)
    random_star(length)
    random_star(length)
    random_star(length)
    random_star(length)
    random_star(length)
    random_star(length)
    random_star(length)
    random_star(length)
    random_star(length)
    random_star(length)
    random_star(length)
    random_star(length)
    random_star(length)
    random_star(length)
    random_star(length)
    random_star(length)
    random_star(length)
    random_star(length)
    random_star(length)
    random_star(length)
    random_star(length)
    random_star(length)
    random_star(length)
    random_star(length)
    random_star(length)
    random_star(length)
    random_star(length)
    random_star(length)
    random_star(length)
    random_star(length)
    random_star(length)
    random_star(length)
    random_star(length)
    random_star(length)
    random_star(length)
    random_star(length)
    random_star(length)
    random_star(length)
    random_star(length)
    random_star(length)
    random_star(length)
    random_star(length)
    random_star(length)
    random_star(length)
    random_star(length)
    random_star(length)
    random_star(length)
    random_star(length)
    random_star(length)
    random_star(length)
    random_star(length)
    random_star(length)
    random_star(length)
    random_star(length)
    random_star(length)
    random_star(length)
    random_star(length)
    random_star(length)
    random_star(length)
    random_star(length)
    random_star(length)
    random_star(length)
    random_star(length)
    random_star(length)
    random_star(length)
    random_star(length)
    random_star(length)
    random_star(length)
    random_star(length)
    random_star(length)
    random_star(length)
    random_star(length)
    random_star(length)
    random_star(length)
    random_star(length)
    random_star(length)
    random_star(length)
    random_star(length)
    random_star(length)
    random_star(length)
    random_star(length)
    random_star(length)
    random_star(length)
    random_star(length)
    random_star(length)
    random_star(length)
    random_star(length)
    random_star(length)
    random_star(length)
    random_star(length)
    random_star(length)
    random_star(length)
    random_star(length)
    random_star(length)
    random_star(length)
    random_star(length)
    random_star(length)
    random_star(length)
    random_star(length)
    random_star(length)
    random_star(length)
    random_star(length)
    random_star(length)
    random_star(length)
    random_star(length)
    random_star(length)
    random_star(length)
    random_star(length)
    random_star(length)
    random_star(length)
    random_star(length)
    random_star(length)
    random_star(length)
    random_star(length)
    random_star(length)
    random_star(length)
    random_star(length)
    random_star(length)
    random_star(length)
    random_star(length)
    random_star(length)
    random_star(length)
    random_star(length)
    random_star(length)
    random_star(length)
    random_star(length)
    random_star(length)
    random_star(length)
    random_star(length)
    random_star(length)
    random_star(length)
    random_star(length)
    random_star(length)
    random_star(length)
    random_star(length)
    random_star(length)
    random_star(length)
    random_star(length)
    random_star(length)
    random_star(length)
    random_star(length)
    random_star(length)
    random_star(length)
    random_star(length)
    random_star(length)
    random_star(length)
    random_star(length)
    random_star(length)
    random_star(length)
    random_star(length)
    random_star(length)
    random_star(length)
    random_star(length)
    random_star(length)
    random_star(length)
    random_star(length)
    random_star(length)
    random_star(length)
    random_star(length)
    random_star(length)
    random_star(length)
    random_star(length)
    random_star(length)
    random_star(length)
    random_star(length)
    random_star(length)
    random_star(length)
    random_star(length)
    random_star(length)
    random_star(length)
    random_star(length)
    random_star(length)
    random_star(length)
    random_star(length)
    random_star(length)
    random_star(length)
    random_star(length)
    random_star(length)
    random_star(length)
    random_star(length)
    random_star(length)
    random_star(length)
    random_star(length)
    random_star(length)
    random_star(length)
    random_star(length)
    random_star(length)
    random_star(length)
    random_star(length)
    random_star(length)
    random_star(length)
    random_star(length)
    random_star(length)
    random_star(length)
    random_star(length)
    random_star(length)
    random_star(length)
    random_star(length)
    random_star(length)
    random_star(length)
    random_star(length)
    random_star(length)
    random_star(length)
    random_star(length)
    random_star(length)
    random_star(length)
    random_star(length)
    random_star(length)
    random_star(length)
    random_star(length)
    random_star(length)
    random_star(length)
    random_star(length)
    random_star(length)
    random_star(length)
    random_star(length)
    random_star(length)
    random_star(length)
    random_star(length)
    random_star(length)
    random_star(length)
    random_star(length)
    random_star(length)
    random_star(length)
    random_star(length)
    random_star(length)
    random_star(length)
    random_star(length)
    random_star(length)
    random_star(length)
    random_star(length)
    random_star(length)
    random_star(length)
    random_star(length)
    random_star(length)
    random_star(length)
    random_star(length)
    random_star(length)
    random_star(length)
    random_star(length)
    random_star(length)
    random_star(length)
    random_star(length)
    random_star(length)
    random_star(length)
    random_star(length)
    random_star(length)
    random_star(length)
    random_star(length)
    random_star(length)
    random_star(length)
    random_star(length)
    random_star(length)
    random_star(length)
    random_star(length)
    random_star(length)
    random_star(length)
    random_star(length)
    random_star(length)
    random_star(length)
    random_star(length)
    random_star(length)
    random_star(length)
    random_star(length)
    random_star(length)
    random_star(length)
    random_star(length)
    random_star(length)
    random_star(length)
    random_star(length)
    random_star(length)
    random_star(length)
    random_star(length)
    random_star(length)
    random_star(length)
    random_star(length)
    random_star(length)
    random_star(length)
    random_star(length)
    random_star(length)
    random_star(length)
    random_star(length)
    random_star(length)
    random_star(length)
    random_star(length)
    random_star(length)
    random_star(length)
    random_star(length)
    random_star(length)
    random_star(length)
    random_star(length)
    random_star(length)
    random_star(length)
    random_star(length)
    random_star(length)
    random_star(length)
    random_star(length)
    random_star(length)
    random_star(length)
    random_star(length)
    random_star(length)
    random_star(length)
    random_star(length)
    random_star(length)
    random_star(length)
    random_star(length)
    random_star(length)
    random_star(length)
    random_star(length)
    random_star(length)
    random_star(length)
    random_star(length)
    random_star(length)
    random_star(length)
    random_star(length)
    random_star(length)
    random_star(length)
    random_star(length)
    random_star(length)
    random_star(length)
    random_star(length)
    random_star(length)
    random_star(length)
    random_star(length)
    random_star(length)
    random_star(length)
    random_star(length)
    random_star(length)
    random_star(length)
    random_star(length)
    random_star(length)
    random_star(length)
    random_star(length)
    random_star(length)
    random_star(length)
    random_star(length)
    random_star(length)
    random_star(length)
    random_star(length)
    random_star(length)
    random_star(length)
    random_star(length)
    random_star(length)
    random_star(length)
    random_star(length)
    random_star(length)
    random_star(length)
    random_star(length)
    random_star(length)
    random_star(length)
    random_star(length)
    random_star(length)
    random_star(length)
    random_star(length)
    random_star(length)
    random_star(length)
    random_star(length)
    random_star(length)
    random_star(length)
    random_star(length)
    random_star(length)
    random_star(length)
    random_star(length)
    random_star(length)
    random_star(length)
    random_star(length)
    random_star(length)
    random_star(length)
    random_star(length)
    random_star(length)
    random_star(length)
    draw_world(350, 350, 20, "Red")
    draw_world(200, 200, 40, "Blue")
    draw_world(0, 0, 60, "Green")
    draw_world(-200, -200, 80, "Yellow")
    draw_world(-400, -400, 100, "White")

def main():
    """
    Should ultimately draw a night sky filled with stars and planets.
    """
    input("Press enter to start: ")
    turtle.bgcolor("black")
    tweak(True, 0)
    length = random.randint(5, 10)
    """Operand error msg, float/int/str errors regarding the length, showed up in terminal as type error...decided to call it specifically an int because before length was a str and it could not do the multiplication/math."""
#   length = input("Enter length of star to draw: ")
#   random_star(length)
#   draw_world(300, 0, 100, "red")
#   draw_star(length)
    draw_celestial_bodies(length)
    tweak(True, 0)
    """Attribute Error, The original line was turtle.hide which is incorrect and it should be turtle.hideturtle, it did not understand that function/variable in the module and as a result ignored it, It showed up in the terminal and showed be the type of error and saying it was invalid, simple easy fix."""
    turtle.hideturtle()
    input("Press enter to end: ")

main()

#END