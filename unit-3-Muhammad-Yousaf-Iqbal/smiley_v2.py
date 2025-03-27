import turtle

def draw_circle(xcor, ycor, radius, fill_color):
    turtle.penup()
    turtle.goto(xcor, ycor)
    turtle.pendown()
    turtle.fillcolor(fill_color)
    turtle.begin_fill
    turtle.circle(radius)
    turtle.end_fill
    turtle.penup()

def draw_centered_circle(xcor, ycor, radius, fill_color):
    #tell the turtle to go to a specific point (xcor, ycor) and setup a heading at 90.
    #tell the turtle to stay centered in the circle point at all time and return to it when done creating circle.
    #tell the turtle to (x+radius, y)
    #draw the circle...
    #put the turtle back in center by using turtle.goto
    turtle.penup()
    turtle.goto(xcor+radius, ycor)
    turtle.left(90)
    turtle.pendown()
    turtle.fillcolor(fill_color)
    turtle.begin_fill()
    turtle.circle(radius)
    turtle.end_fill()
    turtle.penup()
    turtle.setheading(0)
    turtle.goto(xcor, ycor)

def draw_smiley(xcor, ycor, radius, head_color, nose_color):
    draw_centered_circle(xcor, ycor, radius, head_color)
    draw_centered_circle(xcor, ycor, radius/10, nose_color)

def tweak(speed, tracer):
    turtle.speed(speed)
    turtle.tracer(tracer)

def draw_eye(x, y, radius, iris_color):
    draw_centered_circle(x, y, radius, "white")
    draw_centered_circle(x, y, radius/2, "blue")
    draw_centered_circle(x, y, radius/4, "black")

def draw_mouth(x, y, radius, fill_color):
    turtle.goto(-100, 40)
    turtle.setheading(180)
    turtle.pendown()
    turtle.fillcolor(fill_color)
    turtle.begin_fill()
    turtle.forward(radius)
    turtle.left(90)
    turtle.circle(radius, 180)
    turtle.left(90)
    turtle.forward(radius)
    turtle.end_fill()
    turtle.penup()

def main():
    input("Press enter to start...")
    turtle.speed(0)
    draw_smiley(-100, 100, 200, "yellow" , "pink")
    draw_eye(-180, 200, 50, "blue")
    draw_eye(-20, 200, 50, "blue")
    draw_mouth(0, 0, 100, "black")
    turtle.hideturtle()
    input("Press enter to exit...")

main()