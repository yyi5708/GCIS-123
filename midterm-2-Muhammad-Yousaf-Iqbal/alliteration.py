"""
A narrow definition of an alliteration is a sentence, consisting of at least 2
words, with all words beginning with the same letter.  Complete the function
below to:
  - raise a ValueError if the given sentence is empty or consists of only one
    word
  - return True if all words in the sentence begin with the same letter,
    regardless of case, e.g. "P" == "p"
  - return False, otherwise

Unit tests have been provided in alliteration_test.py.  Do not alter any of the
tests.  All tests should pass for your solution to be complete.

Hint: recall that the lower() function will transform a string to all lowercase,
e.g. 
  a_string = "PenGuiN"
  print(a_string.lower())  # prints "penguin"
"""
def is_alliteration(sentence):
    sentence = [sentence]
    print(sentence)
    if sentence == ['']:
        raise(ValueError)
    if [0] in sentence == '':
       raise(ValueError)
    if [1] in sentence == '':
       raise(ValueError)
    if [0] in sentence == [1] in sentence:
       return(True)
    else:
       return(False)

#Done