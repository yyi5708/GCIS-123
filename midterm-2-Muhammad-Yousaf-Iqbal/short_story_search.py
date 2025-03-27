'''
Write a function that uses regular expressions to search "Short_Story.txt" in the data directory

You must find the following words even if its part of word
tower
spirit
tangle
clear

Count the numnber of times you found the word and print the results like this:

Total count for "tower" 2
Total count for "spirit" 12
Total count for "tangle" 3
Total count for "clear" 2
'''

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
    print("Total count is", x)

def main():
    word_search("data/Short_Story.txt")
    word_search("data/Short_Story.txt")
    word_search("data/Short_Story.txt")
    word_search("data/Short_Story.txt")

main()