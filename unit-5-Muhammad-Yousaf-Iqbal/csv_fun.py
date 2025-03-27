import csv
import re

def opener(filename):
    try:
        with open(filename) as _:
            return True
    except FileNotFoundError:
        print("File cannot be opended:", filename)
        return False

def names_and_adresses(filename):
    with open (filename) as csv_file:
        for line in csv_file:
            line.split(",")
            full_name = [0]
            address = [1]
            print("name: ", full_name, "adress: ", address)

def first_only(filename):
    with open(filename) as csv_file:
        csv_reader = csv.reader(csv_file)
        next(csv_reader)
        for record in csv_reader:
            print(record[0])
            print(record[1])

def average(filename, column):
    with open(filename) as csv_file:
        total = 0
        count = 0
    for line in csv_file:
        csv_reader = csv.reader(csv_file)
        next(csv_reader)
        for record in csv_reader:
            tokens = line.split(",")
            grades = tokens[column]
            grades = float(grades)
            total += grades
            count += 1
    average = total / count
    print(average)

def zip_check(filename):
    with open(filename) as csv_file:
        csv_reader = csv.reader(csv_file)
        next(csv_reader)
    for match in re.findall("\d[789]+", filename):
        print(match)

def main():
   opener("data/full_grades_010.csv")
   opener("data/no_file.csv")
   names_and_adresses("data/full_grades_010.csv")
   first_only("data/full_grades_010.csv")
   average("data/full_grades_010.csv", 3)
   average("data/full_grades_010.csv", 28)
   zip_check("data/full_grades_010.csv")

main()