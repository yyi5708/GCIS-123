def variable_practice():
    age = 226
    days = 365
    pet = "Coco"
    pi = 3.1415
    print(age, days, pet, pi)

def expressions_practice():
    exponent = 1**1
    multiplication = 1*1
    division = 1/1
    floor_division = 1//1
    mod = 1%1
    addition = 1+1
    subtraction = 1-1
    print(exponent, multiplication, division, floor_division, mod, addition, subtraction)

#Takes input from user and does math!
def prompt_and_print():
    one = float(input("(1) Enter a numeric value: "))
    two = float(input("(2) Enter a numeric value: "))
    float(one)
    float(two)
    adding = one + two
    subtracting = one - two
    multiplying = one * two
    dividing = one / two
    print(adding, subtracting, multiplying, dividing)

def main():
    variable_practice()
    expressions_practice()
    prompt_and_print()

main()