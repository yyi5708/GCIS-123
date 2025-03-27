PI = (3.14159)

def add(x,y):
    solution = x + y
    return solution

def subtract(x,y):
    solution = x - y
    return solution

def multiply(x,y):
    solution = x * y
    return solution

def divide(x,y):
    solution = x / y
    return solution

def circle_circumference(radius):
    solution = 2 * PI * radius
    return solution

def circle_area(radius):
    solution = PI * radius ** 2
    return solution

def main():
    x = float(input("Enter the first numeric value: "))
    y = float(input("Enter the second numeric value: "))
    A = add(x,y)
    print("Add:",A)
    S = subtract(x,y)
    print("Subtract:",S)
    M = multiply(x,y)
    print("Multiply:",M)
    D = divide(x,y)
    print("Divide:",D)
    CC = circle_circumference(x)
    print("Circle Circumference:",CC)
    CA = circle_area(y)
    print("Circle Area:",CA)

main()