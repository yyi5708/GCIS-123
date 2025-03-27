#MYI

import turtle

def convert_height():
    height_in_inches = int(input("Enter your height in inches: "))
    convert_1 = height_in_inches // 12.00
    convert_2 = height_in_inches % 12.00
    print("You are ",convert_1,"' ",convert_2,"''"," tall", sep="")

def snow_man(fillcolor, pencolor, radius, x, y):
    turtle.penup()
    turtle.bgcolor("Cyan")
    turtle.pensize(5.00)
    turtle.pencolor(pencolor)
    turtle.fillcolor(fillcolor)
    turtle.goto(x, y)
    turtle.pendown()
    turtle.begin_fill()
    turtle.circle(radius)
    turtle.end_fill()
    turtle.penup()

def main():
    convert_height()
    input("Press enter to start: ")
    snow_man ("White", "Black", 100.00, 0.00, -200.00)
    snow_man ("White", "Black", 75.00, 0.00, 0.00)
    snow_man ("White", "Black", 56.25, 0.00, 150.00)
    input("Press enter to exit: ")

main()