"""
Code for functions.py that uses user input to calculate the users age in months and prints a string.
Code by MYI.
"""

"""
Function "time" with different variables, inputs, to calculate desired value and prints it.
"""

#FUNCTION TIME
def time():
    current_year = float(input("Enter the current year: "))
    current_month = float(input("Enter the current month: "))
    birth_year = float(input("Enter your birth year: "))
    birth_month = float(input("Enter your birth month: "))
    age_in_months = ((current_year-birth_year)*12+(current_month-birth_month))
    print("Your age in months is: ", age_in_months)

"""
Function "main" that runs/executes all programs/functions.
"""

#FUNCTION MAIN
def main():
    time()
    time()

#Deploys main function
main()