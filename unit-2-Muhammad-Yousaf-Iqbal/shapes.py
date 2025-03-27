"""
Code for shapes.py that uses user input to calculate different areas, volumes, etc. of different shapes and prints out the input values and computed values.
Code by MYI.
"""

"""
Function "shapes" with different variables, inputs, to calculate desired values and prints it.
"""

#FUNCTION SHAPES
def shapes():
    #CIRCLE
    radius = float(input("Please enter the radius of a circle: "))
    area_of_circle = (3.14*radius*radius)
    print("Radius: ", radius)
    print("The area of a circle is: ", area_of_circle)

    #SPHERE
    radius_sphere = float(input("Please enter the radius of a sphere: "))
    volume_of_sphere = ((1.33*3.14)*radius_sphere**3)
    print("Radius: ",radius_sphere)
    print("The volume of a sphere is: ", volume_of_sphere)

    #RECTANGLE
    height = float(input("Please enter the height of a rectangle: "))
    width = float(input("Please enter the width of a rectangle: "))
    area_of_rectangle = (height*width)
    print("Height: ",height)
    print("Width: ",width)
    print("The area of a rectangle is: ", area_of_rectangle)

    #SQUARE
    side_length = float(input("Please enter the side length of a square: "))
    area_of_square = (side_length*side_length)
    print("Length: ",side_length)
    print("The area of a square is: ", area_of_square)

    #ISOSCELES TRIANGLE
    isosceles_leg = float(input("Please enter the length of a isosceles triangle: "))
    isosceles_height = float(input("Please enter the height of a isosceles triangle: "))
    area_of_isosceles_triangle = (isosceles_leg*isosceles_height/2) #YOU GUYS HAVE THE ANSWER WRONG IN THE ASSIGNMENT, ITS NOT 12, ITS 10 (BASE TIMES HEIGHT DIVIDED BY 2)
    print("Length: ",isosceles_leg)
    print("Height: ",isosceles_height)
    print("The area of a isosceles triangle is: ", area_of_isosceles_triangle)

    #EQUILATERAL TRIANGLE
    equilateral_leg = float(input("Please enter the length of a equilateral triangle: "))
    area_of_equilateral_triangle = (1.73/4*equilateral_leg**2)
    print("Length: ",equilateral_leg)
    print("The area of a equilateral triangle is: ", area_of_equilateral_triangle)

    #TRAPEZOID
    trapezoid_base_1 = float(input("Please enter the first base of a trapezoid: "))
    trapezoid_base_2 = float(input("Please enter the second base of a trapezoid: "))
    trapezoid_height = float(input("Please enter the first height of a trapezoid: "))
    area_of_trapezoid = ((trapezoid_base_1+trapezoid_base_2)/2)*trapezoid_height
    print("First Base: ",trapezoid_base_1)
    print("Second Base: ",trapezoid_base_2)
    print("Height: ",trapezoid_height)
    print("The area of a trapezoid is: ", area_of_trapezoid)

"""
Function "main" that runs/executes all programs/functions.
"""

#FUNCTION MAIN
def main():
    shapes()
    shapes()

#Deploys main function
main()