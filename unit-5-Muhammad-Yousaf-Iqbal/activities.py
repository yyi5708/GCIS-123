import math

def numbers():
    pass

def division():
    while 1==1:
        numerator = float(input("Enter a numerator: "))
        denominator = float(input("Enter a denominator: "))
        result = numerator / denominator
        return result
    if denominator == 0:
        raise ZeroDivisionError("Can't divide by zero.")
    
def password():
    password = input("Enter a password: ")
    x = len(password)
    if x < 10:
        raise ValueError("Password is too short.")
    if x > 20:
        raise ValueError("Password is too long.")
    verify = input("Enter your password again: ")
    if verify == password:
        return password
    if verify != password:
        raise ValueError("Passwords don't match.")

def main():
    #numbers()
    #x = division()
    #print(x)
    #x = password()
    #print(x)
    pass

main()