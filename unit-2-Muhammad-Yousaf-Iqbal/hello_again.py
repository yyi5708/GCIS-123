"""
Code for hello_again.py that uses user input to print a string. Two versions provided with/without "sep".
Code by MYI.
"""

"""
Old version without "sep".
"""

#OLD VERSION
print("(OLD VERSION)")
name = input("Enter your name: ")
print("Hello, again,", name,"!")

#PRINT NEW LINE
print("\n")

"""
New version with "sep".
"""

#NEW VERSION
print("(NEW VERSION)")
name = input ("Enter your name: ")
print("Hello," " again, " "", name,"" "!", sep="")