#Muhammad Yousaf Iqbal

import plotter
import re
import csv

def plot_grades(infile, first_name, last_name):

    with open(infile) as csv_file:
        for row in csv_file:
            csv_reader = csv.reader(csv_file)
            next(csv_reader)
            for record in csv_reader:
                first_name = [0]
                last_name = [1]
                g = [3-27]
                plotter.init(first_name and last_name, "Scale", "Score")
                plotter.add_data_point(g)
                plotter.plot()
                input("Press enter to quit: ")

def put_grades(infile, outfile, last_name):

    with open(infile) as csv_file: 
        outfile = open("./outrows.txt", "w", newline="")
        writer = csv.writer(outfile, quoting=csv.QUOTE_MINIMAL)
        for row in csv.reader:
            writer.writerow(row)
            next(csv.reader)
            for record in csv.reader:
                last_name = [1]
                return last_name

def get_average(filename, student_last_name):

    with open(filename) as csv_file:
        total = 0
        count = 0
    for row in csv_file:
        csv_reader = csv.reader(csv_file)
        next(csv_reader)
        for record in csv_reader:
            tokens = row.split(",")
            grade = tokens[student_last_name]
            grade = float(grade)
            total += grade
            count += 1
    average = total / count
    return("Student Name: ", student_last_name, "Grade Average (Mean): ", average)

def main():
    
    input("Press enter to start: ")
    plot_grades("data/full_grades_010.csv", "Vanderberg", "Ileana")
    put_grades("data/full_grades_010.csv", "outrows.txt", "Ileana")
    get_average("data/full_grades_100.csv", "Gommer")
    get_average("data/full_grades_100.csv", "Coldivar")
    input("Press enter to end: ")

main()