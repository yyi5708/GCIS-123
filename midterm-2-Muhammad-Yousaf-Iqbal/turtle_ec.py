'''
Match The turtle_ec.png Image for 3 Bonus Points
Recursion Mandatory
'''
import turtle

def draw_spiral_squares(size, angle, depth):
    turtle.speed('fastest')
    turtle.pendown()
    turtle.forward(size)
    turtle.left(angle)
    turtle.forward(depth)
    turtle.left(angle)
    turtle.forward(size)
    turtle.left(angle)
    turtle.forward(depth)
    turtle.left(angle)
    turtle.penup()
    draw_spiral_squares(size+10, angle+1, depth+10)

def main():
    draw_spiral_squares(10, 90, 10)
    input()

main()