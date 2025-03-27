#Muhammad Yousaf Iqbal

import csv
import re

def find_rabbit(filename):
    
    count = 0
    with open(filename) as csv_file:
        csv_reader = csv.reader(csv_file)
        next(csv_reader)
        for record in csv_reader:
            Rabbit = record[0]
            if "Rabbit" in Rabbit:
                count += 1
    return count

def find_rabbit_regex(filename):
    
    count = 0
    with open(filename) as csv_file:
        csv_reader = csv.reader(csv_file)
        next(csv_reader)
        for record in csv_reader:
            Rabbit = record[0]
            for match in re.findall("Rabbit", Rabbit):
                count += 1
    return count

def main():
    
    print("Found Rabbit", find_rabbit("alice.txt"), "times.")
    print("Found Rabbit", find_rabbit_regex("alice.txt"), "times.")
    
if __name__ == "__main__":
    main()

#Done