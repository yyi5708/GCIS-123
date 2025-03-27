#Muhammad Yousaf Iqbal

import csv
import plotter
import token

def terminate():
    answer = input("Are you sure you want to quit? (Y/N) ")
    if answer == "Y" or "y":
        return True
    if answer == "N" or "n":
        return False
    else:
        print("Error! (Y/N) ")

def plot_grades(filename, first_name, last_name):
    with open(filename) as csv_file:
        reader = csv.reader(csv_file)
        next(reader).split(",")
        first_name_index = token[1]
        last_name_index = token[0]
        grade_index = token[2-17]
        plotter.init("Grades For " + last_name, "Student", "Scores")
        for row in reader:
            if row[first_name_index] == first_name and row[last_name_index] == last_name:
                fields = row.split(",")
                score = float(fields[grade_index])
                plotter.add_data_point(score)
                plotter.plot()
                return True
            if grade_index == "" or "0":
                raise ValueError(plotter.add_data_point(0.0))
    return False

def student_grades(tokens):
    filename = tokens[1]
    first_name = tokens[2]
    last_name = tokens[3]
    plot = plot_grades(filename, first_name, last_name)
    if plot:
        print("Plot finished (window may be hidden).")
    else:
        print("Plot failed (no such student).")
    return plot

def help():
    print("stu <filename> <first name> <last name> - plot student grades")
    print("item")
    print("quit - quits")
    print("help - displays this message")

def main():
    #x = terminate()
    #print(x)
    while True:
        try:
            user = input(">> ")
            if user.strip() == "":
                raise ValueError("Error!")
            tokens = user.split()
            if tokens[0] == "quit":
                terminate()
                print("Goodbye!")
                break
        except ValueError:
            print("Enter a command or 'quit' to quit.")
        try:
            user = input(">> ")
            tokens = user.split()
            if not tokens:
                raise ValueError("Enter a command or 'quit' to quit.")
            if tokens[0] == "quit":
                terminate()
                print("Goodbye!")
                break
            elif tokens[0] == "stu":
                student_grades(tokens)
            else:
                print("Error!")
        except ValueError:
            print("Usage: stu <filename> <first name> <last name>.")
        except FileNotFoundError:
            print("No such file: ", tokens[1])
        try:
            user = input(">> ")
            tokens = user.split()
            if not tokens:
                raise ValueError("Enter a command or 'quit' to quit.")
            if tokens[0] == "quit":
                terminate()
                print("Goodbye!")
                break
            elif tokens[0] == "stu":
                student_grades(tokens)
            elif tokens[0] == "help":
                help()
            else:
                print("Error!")
        except ValueError:
            print("Usage: stu <filename> <first name> <last name>.")
        except FileNotFoundError:
            print("No such file: ", tokens[1])

main()

#End