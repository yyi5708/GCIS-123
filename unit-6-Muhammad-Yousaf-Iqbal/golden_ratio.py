#Muhammad Yousaf Iqbal

import arrays
import turtle

def fibonacci(N):

    if N <= 0:
        return None
    if N == 1:
        return 0
    if N == 2:
        return 1
    else:
        if N > 2:
            return fibonacci(N-1) + fibonacci(N-2)

def fill_fibonacci_array(array, index=0):

    if index == len(array):
        return ("The Index And The Length Of The Array Are Equal.")
    else:
        array[index] = fibonacci(index)
        fill_fibonacci_array(array, index+1)

def print_ratios(array, index=0):

    a = array[index]
    b = array[index+1]
    if index >= len(array) - 1:
        return ("Reached The End Of The Array.")
    if a == 0:
        print("Undefined")
    if b == 0:
        print("Undefined")
    if a is None:
        print("Undefined")
    if b is None:
        print("Undefined")
    else:
        ratio_1 = b / a
        ratio_2 = (a + b) / b
        x = (f"{a:>4n} {b:>4n} {ratio_1:.5f} {ratio_2:.5f}")
        print(x)
    print_ratios(array, index+1)

def draw_fibonacci_spiral_1():

    array_12 = arrays.Array(12)
    x = fill_fibonacci_array(array_12)
    def draw_square(side_length):
        for i in range(4):
            turtle.forward(side_length)
            turtle.right(90)
    number_squares = len(x)
    turtle.speed(5)
    turtle.penup()
    turtle.goto(0,0)
    turtle.pendown()
    for i in range(number_squares):
        draw_square(3*x[i])
        turtle.penup()
        turtle.forward(3*x[i])
        turtle.right(90)
        turtle.forward(3*x[i])
        turtle.pendown()
    turtle.penup()
    turtle.goto(0,0)
    turtle.setheading(90)
    turtle.pencolor("red")
    turtle.pensize(3)
    turtle.pendown()
    for i in range(number_squares):
        turtle.circle(-5*x[i],90)

def draw_fibonacci_spiral_2():

    fibo_numbers = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
    def draw_square(side_length):
        for i in range(4):
            turtle.speed(0)
            turtle.pensize(2.5)
            turtle.pencolor("Black")
            turtle.forward(side_length)
            turtle.right(90)
    number_squares = len(fibo_numbers)
    turtle.speed(0)
    turtle.penup()
    turtle.goto(0,0)
    turtle.pendown()
    for i in range(number_squares):
        draw_square(3*fibo_numbers[i])
        turtle.penup()
        turtle.forward(3*fibo_numbers[i])
        turtle.right(90)
        turtle.forward(3*fibo_numbers[i])
        turtle.pendown()
    turtle.penup()
    turtle.goto(0,0)
    turtle.setheading(90)
    turtle.pensize(5)
    turtle.pencolor("Red")
    turtle.pendown()
    for i in range(number_squares):
        turtle.circle(-5*fibo_numbers[i],90)

def main():
    
    #print(fibonacci(9))
    #array_21 = arrays.Array(21)
    #fill_fibonacci_array(array_21)
    #print(array_21)
    #array_21 = arrays.Array(21)
    #print_ratios(array_21)
    #print(array_21)
    #input("Press enter to start: ")
    #draw_fibonacci_spiral_1()
    #input("Press enter to end: ")
    #input("Press enter to start: ")
    #draw_fibonacci_spiral_2()
    #input("Press enter to end: ")
    pass

if __name__ == "__main__":

    main()

#Done

