def countup(number):
    number = 5
    sum = 0
    current = 0
    while current < number + 1:
        print(current)
        sum += current
        current += 1    
    return sum

def countdown(number):
    sum = 0
    while number >= 0:
        print(number)
        sum += number
        number -= 1
    return sum

def a_string(string):
    print(a_string)
    length = len(a_string)
    index = 0
    while index < length:
        char = a_string[index]
        print(char)
        index = index + 1
    return

def print_range_1(a_range):
    index = 0
    length = len(a_range)
    while index < length:
        each_number = a_range[index]
        print(each_number)
        index = index + 1
    
def print_range_2(a_range):
    for next in a_range:
        print(next, end="")

def reverse_char(string):
    x = string[::-1]
    print(x)

def main():
    #sum = countdown(5)
    #print("sum:", sum)
    #sum = countup(5)
    #print("sum:", sum)
    #print(a_string)
    #print_range_1("LOSER")
    #print_range_2(range(0,101, 5))
    reverse_char("LOSER")

main()