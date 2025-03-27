#MYI

from palindrome import palindrome

def test_palindrome_odd_length():

    #setup
    (string) = ("hello")
    #invoke
    pass
    #analyze
    assert(palindrome(string) == "hellolleh")

def test_palindrome_even_length():

    #setup
    (string) = ("bad")
    #invoke
    pass
    #analyze
    assert(palindrome(string) == "baddab")

def main():

    pass

if __name__ == "__main__":

    main()

#Done
