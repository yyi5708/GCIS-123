"""
Code for landscape.py that uses turtle to draw various objects, shapes, etc. which are all customizable. By using these shapes/objects, I created a unique landscape with lots of detail and it looks amazing.
Code by MYI.
"""

#importing turtle.
import turtle

"""
Function "rectangle" with different variables, inputs, to draw a customizable rectangle.
"""

#Function rectangle.
def rectangle(width_1, width_2, height, pen_color, fill_color):
    turtle.pendown()
    turtle.pencolor(pen_color)
    turtle.fillcolor(fill_color)
    turtle.begin_fill()
    turtle.forward(width_1)
    turtle.left(height)
    turtle.forward(width_2)
    turtle.left(height)
    turtle.forward(width_1)
    turtle.left(height)
    turtle.forward(width_2)
    turtle.left(height)
    turtle.end_fill()
    turtle.penup()

"""
Function "equilateral_traingle" with different variables, inputs, to draw a customizable equilateral traingle.
"""

#Function equilateral traingle.
def equilateral_traingle(base, angle, pen_color, fill_color):
    turtle.pendown()
    turtle.pencolor(pen_color)
    turtle.fillcolor(fill_color)
    turtle.begin_fill()
    turtle.forward(base)
    turtle.left(angle)
    turtle.forward(base)
    turtle.left(angle)
    turtle.forward(base)
    turtle.left(angle)
    turtle.end_fill()
    turtle.penup()

"""
Function "circle" with different variables, inputs, to draw a customizable circle.
"""

#Function circle.
def circle(radius, pen_color, fill_color):
    turtle.down
    turtle.pencolor(pen_color)
    turtle.fillcolor(fill_color)
    turtle.begin_fill()
    turtle.circle(radius)
    turtle.end_fill()
    turtle.up

"""
Function "main" that runs/executes all programs/functions.
"""

#Function main.
def main():
    #input to start.
    input("Press enter to continue...")
    #background color.
    turtle.bgcolor ("DeepSkyBlue")
    #grass.
    turtle.penup()
    turtle.goto(-800, -420)
    rectangle(1600, 320, 90 , "black" , "Lime")
    #mountain.
    turtle.goto(-800, -100)
    turtle.penup()
    equilateral_traingle(400, 120, "black" , "Gray")
    turtle.goto(400, -100)
    turtle.penup()
    equilateral_traingle(400, 120, "black" , "Gray")
    turtle.goto(-600, -100)
    turtle.penup
    equilateral_traingle(500, 120, "black" , "Gray")
    turtle.goto(0, -100)
    turtle.penup()
    equilateral_traingle(500, 120, "black" , "Gray")
    #sun.
    turtle.goto(-40, 200)
    turtle.penup
    circle(100, "black" , "Yellow")
    #tree.
    turtle.goto(-800, -210)
    turtle.penup()
    rectangle(10, 40, 90, "black" , "SaddleBrown")
    turtle.goto(-795, -180)
    turtle.penup()
    circle(20, "black", "Green")
    turtle.goto(-700, -210)
    turtle.penup()
    rectangle(10, 40, 90, "black" , "SaddleBrown")
    turtle.goto(-695, -180)
    turtle.penup()
    circle(20, "black", "Green")
    turtle.goto(-600, -210)
    turtle.penup()
    rectangle(10, 40, 90, "black" , "SaddleBrown")
    turtle.goto(-595, -180)
    turtle.penup()
    circle(20, "black", "Green")
    turtle.goto(-500, -210)
    turtle.penup()
    rectangle(10, 40, 90, "black" , "SaddleBrown")
    turtle.goto(-495, -180)
    turtle.penup()
    circle(20, "black", "Green")
    turtle.goto(-400, -210)
    turtle.penup()
    rectangle(10, 40, 90, "black" , "SaddleBrown")
    turtle.goto(-395, -180)
    turtle.penup()
    circle(20, "black", "Green")
    turtle.goto(-300, -210)
    turtle.penup()
    rectangle(10, 40, 90, "black" , "SaddleBrown")
    turtle.goto(-295, -180)
    turtle.penup()
    circle(20, "black", "Green")
    turtle.goto(-200, -210)
    turtle.penup()
    rectangle(10, 40, 90, "black" , "SaddleBrown")
    turtle.goto(-195, -180)
    turtle.penup()
    circle(20, "black", "Green")
    turtle.goto(-100, -210)
    turtle.penup()
    rectangle(10, 40, 90, "black" , "SaddleBrown")
    turtle.goto(-95, -180)
    turtle.penup()
    circle(20, "black", "Green")
    turtle.goto(0, -210)
    turtle.penup()
    rectangle(10, 40, 90, "black" , "SaddleBrown")
    turtle.goto(5, -180)
    turtle.penup()
    circle(20, "black", "Green")
    turtle.goto(100, -210)
    turtle.penup()
    rectangle(10, 40, 90, "black" , "SaddleBrown")
    turtle.goto(105, -180)
    turtle.penup()
    circle(20, "black", "Green")
    turtle.goto(200, -210)
    turtle.penup()
    rectangle(10, 40, 90, "black" , "SaddleBrown")
    turtle.goto(205, -180)
    turtle.penup()
    circle(20, "black", "Green")
    turtle.goto(300, -210)
    turtle.penup()
    rectangle(10, 40, 90, "black" , "SaddleBrown")
    turtle.goto(305, -180)
    turtle.penup()
    circle(20, "black", "Green")
    turtle.goto(400, -210)
    turtle.penup()
    rectangle(10, 40, 90, "black" , "SaddleBrown")
    turtle.goto(405, -180)
    turtle.penup()
    circle(20, "black", "Green")
    turtle.goto(500, -210)
    turtle.penup()
    rectangle(10, 40, 90, "black" , "SaddleBrown")
    turtle.goto(505, -180)
    turtle.penup()
    circle(20, "black", "Green")
    turtle.goto(600, -210)
    turtle.penup()
    rectangle(10, 40, 90, "black" , "SaddleBrown")
    turtle.goto(605, -180)
    turtle.penup()
    circle(20, "black", "Green")
    turtle.goto(700, -210)
    turtle.penup()
    rectangle(10, 40, 90, "black" , "SaddleBrown")
    turtle.goto(705, -180)
    turtle.penup()
    circle(20, "black", "Green")
    turtle.goto(800, -210)
    turtle.penup()
    rectangle(10, 40, 90, "black" , "SaddleBrown")
    turtle.goto(805, -180)
    turtle.penup()
    circle(20, "black", "Green")
    #river.
    turtle.goto(-800, -320)
    turtle.penup()
    rectangle(1600, 80, 90 , "black" , "Blue")
    #stone.
    turtle.goto(-695, -385)
    turtle.penup
    circle(15, "black", "Silver")
    turtle.goto(-595, -385)
    turtle.penup
    circle(15, "black", "Silver")
    turtle.goto(-495, -385)
    turtle.penup
    circle(15, "black", "Silver")
    turtle.goto(-395, -385)
    turtle.penup
    circle(15, "black", "Silver")
    turtle.goto(-295, -385)
    turtle.penup
    circle(15, "black", "Silver")
    turtle.goto(-195, -385)
    turtle.penup
    circle(15, "black", "Silver")
    turtle.goto(-95, -385)
    turtle.penup
    circle(15, "black", "Silver")
    turtle.goto(0, -385)
    turtle.penup()
    circle(15, "black", "Silver")
    turtle.goto(95, -385)
    turtle.penup
    circle(15, "black", "Silver")
    turtle.goto(195, -385)
    turtle.penup
    circle(15, "black", "Silver")
    turtle.goto(295, -385)
    turtle.penup
    circle(15, "black", "Silver")
    turtle.goto(395, -385)
    turtle.penup
    circle(15, "black", "Silver")
    turtle.goto(495, -385)
    turtle.penup
    circle(15, "black", "Silver")
    turtle.goto(595, -385)
    turtle.penup
    circle(15, "black", "Silver")
    turtle.goto(695, -385)
    turtle.penup
    circle(15, "black", "Silver")
    #cloud.
    turtle.goto(-695, 335)
    turtle.penup()
    circle(25, "black", "WhiteSmoke")
    turtle.goto(-665, 335)
    turtle.penup()
    circle(25, "black", "WhiteSmoke")
    turtle.goto(-635, 335)
    turtle.penup()
    circle(25, "black", "WhiteSmoke")
    turtle.goto(-605, 335)
    turtle.penup()
    circle(25, "black", "WhiteSmoke")
    turtle.goto(-595, 335)
    turtle.penup()
    circle(25, "black", "WhiteSmoke")
    turtle.goto(-565, 335)
    turtle.penup()
    circle(25, "black", "WhiteSmoke")
    turtle.goto(-535, 335)
    turtle.penup()
    circle(25, "black", "WhiteSmoke")
    turtle.goto(-505, 335)
    turtle.penup()
    circle(25, "black", "WhiteSmoke")
    turtle.goto(685, 335)
    turtle.penup()
    circle(25, "black", "WhiteSmoke")
    turtle.goto(655, 335)
    turtle.penup()
    circle(25, "black", "WhiteSmoke")
    turtle.goto(625, 335)
    turtle.penup()
    circle(25, "black", "WhiteSmoke")
    turtle.goto(595, 335)
    turtle.penup()
    circle(25, "black", "WhiteSmoke")
    turtle.goto(585, 335)
    turtle.penup()
    circle(25, "black", "WhiteSmoke")
    turtle.goto(555, 335)
    turtle.penup()
    circle(25, "black", "WhiteSmoke")
    turtle.goto(525, 335)
    turtle.penup()
    circle(25, "black", "WhiteSmoke")
    turtle.goto(495, 335)
    turtle.penup()
    circle(25, "black", "WhiteSmoke")
    #hide turtle.
    turtle.goto(1000, 1000)
    turtle.penup()
    #input to end.
    input("Press enter to exit...")

#Deploys main function.
main()