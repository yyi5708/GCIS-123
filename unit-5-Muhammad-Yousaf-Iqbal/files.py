import csv
import plotter

def print_lines(filename):
    file = open(filename)
    for line in file:
        line_stripped = line.strip()
        print(line_stripped)

def word_search(filename):
    file = open(filename)
    word = input("Enter a word: ")
    word = word.lower()
    found_it = False
    x = 0
    for line in file:
        file_word = line.strip()
        if word == file_word.lower():
            print("Found the word: ",file_word)
            found_it = True
        if found_it == True:
            break
        x += 1
    if found_it == False:
        print("Didn't find the word.")
    file.close()
    print(x)

def longest_word(string):
    stripped = string.strip()
    longest_word = ""
    if stripped != "":
        words = stripped.split()
        for word in words:
            if len(word) > len(longest_word):
                longest_word = word
    print("The longest words is : ", longest_word)

def longest_words(filename):
    file = open(filename)
    count = 0
    for line in file:
        longest_word(line)
        count += 1
        if count > 100:
            break
    file.close()

def print_names(filename):
    file = open(filename)
    next(file)
    for line in file:
        fields = line.split(",")
        print(fields[1], fields[0])
    file.close()

def plot_grades(filename, column):
    with open (filename) as csv_file:
        header = next(csv_file).split(",")
        name = header[column]
        plotter.init("Grades For " + name, "Students", "Scores")    
        for row in csv_file:
            fields = row.split(",")
            score = float(fields[column])
            plotter.add_data_point(score)
        plotter.plot()

def main():
    #print_lines("data/alice.txt")
    word_search("data/words.txt")
    #longest_word("Hello World! It is almost the weekend.")
    #longest_words("data/alice.txt")
    #print_names("data/grades_010.csv")
    #plot_grades("data/grades_010.csv", 2)
    #input("Press enter to continue: ")

main()