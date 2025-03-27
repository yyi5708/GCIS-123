"""
The CSV file, data/baby_names.csv, contains a sample of yearly counts of baby
names from the years 2012-2021.  Please review this file and ask if you have
any questions.

Find The Most Popular Baby Name Each Year

Example Output:
2012 Bill
2013 Josh
2014 Stefon
"""

import csv

def pop_baby_name_by_year():
    with open("data/baby_names_050.csv") as file:
        reader = csv.DictReader(file)
        next(reader)
        for line in file:
            line.split(",")
            name = line[0:4]
            year = line[8:100]
            print(year, name)
      
def main():
    pop_baby_name_by_year()

main()