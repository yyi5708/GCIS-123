"""
A small program that uses the turtle to draw a stick person.
@author GCCIS Faculty
"""
import turtle

# pen size used to draw the stick person
PEN_SIZE = 4            

# used to determine height based on head radius
BODY_MULTIPLIER = 4

# used to determine arm/leg length based on head radius
LIMB_MULTIPLIER = 2     

# used to determine length of neck based on head radius
NECK_MULTIPLIER = 0.5

# default location of the neck/base of head
NECK_X = 0
NECK_Y = 100

def tweak(speed, tracer):
    """
    Used to adjust the turtle's speed and tracer settings
    """
    turtle.speed(speed)
    turtle.tracer(tracer)

def draw_circle(x, y, radius, color):
    """
    Draws a filled-in circle at the specifed location.
    """
    turtle.up()
    turtle.goto(x, y)
    turtle.down()
    turtle.fillcolor(color)
    turtle.begin_fill()
    turtle.circle(radius)
    turtle.end_fill()

def draw_body(x, y, height):
    """
    Draws the body of the stick person as a line starting at the specified
    location and moving straight down for the specified height.
    """
    turtle.up()
    turtle.goto(x, y)
    turtle.setheading(270)
    turtle.down()
    turtle.forward(height)

def draw_limbs(x, y, length):
    """
    Draws limbs as straight lines at a 90 degree angle that extend for the 
    specified length from the specified apex location.
    """
    turtle.goto(x, y)
    turtle.down()
    turtle.setheading(225)
    turtle.forward(length)
    turtle.goto(x, y)
    turtle.setheading(315)
    turtle.forward(length)
    turtle.up()

def draw_stick_person(x, y, radius, color):
    """
    Draws a complete stick person with the base of the head/neck at the 
    specified location. The radius is used to determine head size and the
    color is used to fill the head.
    """
    turtle.pensize(PEN_SIZE)
    height = radius * BODY_MULTIPLIER
    limb_length = radius * LIMB_MULTIPLIER
    neck_length = radius * NECK_MULTIPLIER
    draw_circle(x, y, radius, color)
    draw_body(x, y, height)
    draw_limbs(x, y-neck_length, limb_length)
    draw_limbs(x, y-height, limb_length)

def main():
    """
    Prompts the user for a radius and draws a stick person of the specified 
    size.
    """
    tweak(1, True)
    radius = input("Enter radius of head: ")
    radius = int(radius)
    draw_stick_person(NECK_X, NECK_Y, radius, "orange")
    turtle.hideturtle()
    input("Press enter to exit...")
    # close the window
    # turtle.Screen().bye()
    # turtle.home()

main()