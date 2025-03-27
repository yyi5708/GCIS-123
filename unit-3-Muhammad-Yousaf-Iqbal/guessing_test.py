#TOP

"""
Program that checks/tests the users inputs of guess/answer values and returns the corresponding strings/messages.
Program for a number guessing game for a value between 1 and 10 (inclusive).
Author: MYI.
"""

"""
Importing modules.
"""

import guessing
import random

"""
Function to test if guess value is less than 1.
"""

def test_check_guess_less_than_1():
    #setup
    answer = 5
    guess = 0
    expected = "Guess is out of range."
    #invoke
    actual = guessing.check_guess(answer, guess)
    #analyze
    assert expected == actual

"""
Function to test if guess value is greater than 10.
"""

def test_check_guess_greater_than_10():
    #setup
    answer = 5
    guess = 100
    expected = "Guess is out of range."
    #invoke
    actual = guessing.check_guess(answer, guess)
    #analyze
    assert expected == actual

"""
Function to test if guess value is less than answer value.
"""

def test_check_guess_less_than_answer():
    #setup
    answer = 5
    guess = 2
    expected = "Guess is too low."
    #invoke
    actual = guessing.check_guess(answer, guess)
    #analyze
    assert expected == actual

"""
Function to test if guess value is greater than answer value.
"""

def test_check_guess_greater_than_answer():
    #setup
    answer = 5
    guess = 9
    expected = "Guess is too high."
    #invoke
    actual = guessing.check_guess(answer, guess)
    #analyze
    assert expected == actual

"""
Function to test is guess value is equal to answer value.
"""

def test_check_guess_equal_to_answer():
    #setup
    answer = 5
    guess = 5
    expected = "Guess is correct."
    #invoke
    actual = guessing.check_guess(answer, guess)
    #analyze
    assert expected == actual

"""
Function for main to run/execute all functions.
Function for the number guessing game and works as expected.
"""

def main():
    #set guessing counter to 0
    guess_counter = 0
    #set answer to a random integer value ranging from 1 to 10 (inclusive)
    answer = random.randint(1,10)
    #set a loop while the guessing counter is less than 3
    while guess_counter < 3:
        #set guess to a user input integer value
        guess = int(input("Enter guess: "))
        #add 1 to the guess counter
        guess_counter += 1
        #if guess is less than 1
        if guess < 1:
            print("Guess is out of range.")
        #if guess is greater than 10
        if guess > 10:
            print("Guess is out of range.")
        #if guess is less than answer
        if guess < answer:
            print("Guess is too low.")
        #if guess is greater than answer
        if guess > answer:
            print("Guess is too high.")
        #if guess is equal to answer...(1)
        if guess == answer:
            break
    #if guess is equal to answer...(2)
    if guess == answer:   
        print("Guess is correct.")
        print("Game over.")
    #else...
    else:
        print("The correct answer was:",answer)
        print("Game over.")

"""
Deploy main function.
"""

main()

#BOTTOM