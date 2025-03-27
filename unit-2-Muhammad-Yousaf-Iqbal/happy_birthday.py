#prompt for function
def bday_message():
    #prompt for name
    name = input("What is your name: ")
    #prompt for month
    month = input("What is your birth month: ")
    #prompt for day
    day = input("What is your birth day: ")
    #prompt for year
    year = input("What is your birth year: ")
    #prompt for birthday message
    print(name,",","your birthday is on",month,day,",",year,"!")

#prompt for main
def main():
    bday_message()
    bday_message()
    bday_message()
    bday_message()

main()