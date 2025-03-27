#Muhammad Yousaf Iqbal

def pi_tester():

    pi = "3.1415926535897932384626433832795028841971693993751058209749445923078164062862089986280348253421170679"
    count = 0
    for x in range(100):
        number = input("Enter the decimal digits of pi in order: ")
        if number == pi[x]:
            count += 1
        else:
            print("\n")
            print("You entered the wrong decimal digit of pi. The correct decimal digit of pi is: ",pi[x])
            break
        if count == 100:
            print("\n")
            print("You have successfully entered the first 100 decimal digits of pi in order.")
            break
    print("\n")
    return (count)

def display_score(score):

    if score < 0:
        print("Error, score cannot be less than 0 or a negative number.")
    if score >= 0 and score <= 4:
        print("You entered",score,"correct decimal digits of pi in order. You are a PI Neophyte.")
    if score >= 5 and score <= 9:
        print("You entered",score,"correct decimal digits of pi in order. You are a PI Novice.")
    if score >= 10 and score <= 24:
        print("You entered",score,"correct decimal digits of pi in order. You are a PI Journeyman.")
    if score >= 25 and score <= 49:
        print("You entered",score,"correct decimal digits of pi in order. You are a PI Enthusiast.")
    if score >= 50 and score <= 96:
        print("You entered",score,"correct decimal digits of pi in order. You are a PI Connoisseur.")
    if score >= 97 and score <= 100:
        print("You entered",score,"correct decimal digits of pi in order. You are a PI Expert.")
    if score >= 101:
        print("You entered",score,"correct decimal digits of pi in order. You are a PI Imposter.")

def main():

    print("\n")
    x = pi_tester()
    print(x)
    print("\n")
    display_score(x)
    print("\n")

main()

#DONE