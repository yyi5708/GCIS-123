#TOP

"""
Program that checks the answer and guess values and compares them both and returns a string message.
Author: MYI.
"""

"""
Function for checking with the user inputs of answer and guess.
"""

def check_guess(answer, guess):
    #guess less than 1.
    if guess < 1:
        return "Guess is out of range."
    #guess greater than 10.
    if guess > 10:
        return "Guess is out of range."
    # guess less than answer.
    if guess < answer:
        return "Guess is too low."
    #guess greater than answer.
    if guess > answer:
        return "Guess is too high."
    #guess equal to answer.
    if guess == answer:
        return "Guess is correct."

#BOTTOM