"""
Pick a number 1 to 10
"""

import random

def check_guess (guess, answer):
    """
    Check to see if the guess was correct.
    """
    if guess == answer :
        return 0
    elif guess > answer:
        print ("Guess too high")
        return guess - answer
    else:
        print ("Guess too low")
        return answer - guess
        
def main ():

    answer = random.randint(1,10)

    guess = int (input ("Guess a nbr between 1 and 10: "))

    if guess < 1 or guess > 10:
        print ("Invalid number, It must be between 1 and 10")
    else:

        diff = check_guess (guess,answer)

        if diff == 0:
            print ("You guessed the number", answer)
        else:
            print ("You guess was", diff, "away from the number")


if __name__ == "__main__":
   main ()