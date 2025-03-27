#MYI

def palindrome(string):

    if (string[-1] in ["a", "e", "i", "o", "u"]):
        #odd length
        return(string + string[-2::-1])
    else:
        #even length
        return(string + string[::-1])

def main():

    (string) = input("enter a string: ")
    (palindrome_string) = palindrome(string)
    print("palindrome:", palindrome_string)

if __name__ == "__main__":

    main()

#Done
