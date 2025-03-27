import random

def is_correct(guess, answer):
    return answer == guess

def check_guess(guess, answer):
    if answer == guess:
        return 0
    elif guess > answer:
        difference = guess - answer
        return difference
    else:
        return answer - guess

def main():
    answer = random.randint(1,10)
    guess = input("Guess a number from 1 to 10: ")
    guess = int(guess)
    check_guess(guess, answer)
    if is_correct(guess, answer):
        print("You got it!")
    else:
        print("Wrong! Try again.")
    result = check_guess(guess, answer)
    if result == 0:
        print("You guessed the number!")
    else:
        print("Your guess was", + result, "away from the number.")

if __name__== "__main__":
        main()