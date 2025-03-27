import turtle

def draw_circle(fillcolor, radius, x, y):
    turtle.penup()
    turtle.fillcolor(fillcolor)
    turtle.goto(x, y)
    turtle.pendown()
    turtle.begin_fill()
    turtle.circle(radius)
    turtle.end_fill()
    turtle.penup()

def draw_centered_circle(fillcolor, radius, x, y):
    turtle.penup()
    turtle.fillcolor(fillcolor)
    turtle.goto(x, y)    
    turtle.forward(radius)
    turtle.left(90)
    turtle.pendown()
    turtle.begin_fill()
    turtle.circle(radius)
    turtle.end_fill()
    turtle.left(90)
    turtle.penup()
    turtle.forward(radius)
    turtle.left(180)

def draw_smiley(fillcolor, radius, x, y):
    draw_centered_circle(fillcolor, radius, x, y)

def tweak(speed, tracer):
    turtle.speed(speed) # 1 to 10
    turtle.tracer(tracer) # True or False

def draw_eye(fillcolor, radius, x, y):
    draw_centered_circle(fillcolor, radius, x, y)

def draw_mouth(fillcolor, radius, x, y):
    turtle.goto(x, y)
    turtle.setheading(180)
    turtle.pendown()
    turtle.fillcolor(fillcolor)
    turtle.begin_fill()
    turtle.forward(radius)
    turtle.left(90)
    turtle.circle(radius, 180)
    turtle.left(90)
    turtle.forward(radius)
    turtle.end_fill()
    turtle.penup()

def main():
    #draw_circle("Yellow", 50, 0, 0)
    #draw_circle("Orange", 40, 100, 100)
    #draw_circle("Red", 30, -100, 100)
    #draw_centered_circle("Yellow", 100, 0, 0)
    tweak(10, False)
    turtle.bgcolor("White")
    turtle.pencolor("Black")
    turtle.pensize(2.5)
    draw_smiley("Yellow", 250, 0, 0)
    draw_smiley("Pink", 25, 0, 0)
    draw_eye("White", 50, 100, 100)
    draw_eye("Blue", 25, 100, 100)
    draw_eye("Black", 12.5, 100, 100)
    draw_eye("White", 50, -100, 100)
    draw_eye("Blue", 25, -100, 100)
    draw_eye("Black", 12.5, -100, 100)
    draw_mouth("Black", 150, 0, -75)
    turtle.hideturtle()
    input("EXIT? ")

main()