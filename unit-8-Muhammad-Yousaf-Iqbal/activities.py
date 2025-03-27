import random

def inserter(a_list, value):
    middle = len(a_list) / 2
    a_list.insert(middle, value)

def popper(a_list):
    length = len(a_list)
    if length > 0:
        index = random.randrange(length)
        popped = a_list.pop(index)
        print(a_list, popped)
        popper(a_list)

def packer():
    return True, 1, "abc", 3.14159

def swapper(a_list):
    length = len(a_list)
    midpoint = length // 2
    for i in range(midpoint):
        a_list[i], a_list[midpoint + i] = a_list[midpoint + i], a_list[i]
    return a_list

def chunky(a_list, size):
    start = 0
    stop = size
    chunk = a_list[start:stop]
    while chunk:
        print(chunk)
        start = stop
        stop = start + size
        chunk = a_list[start:stop]

def sevens_key(number):
    string = str(number)
    if string[0] == "7":
        return 0
    else:
        return 100

def lucky_7s(a_list):
    print(a_list)
    a_list.sort(key=sevens_key)
    print(a_list)

def comprehension():
    pass

def make_table(rows, columns, value=0):
    pass

def main():
    #a_list = [1, 2, 3, 4]
    #print(a_list)
    #inserter(a_list, 12)
    #print(a_list)
    #print("Its popping time \n")
    #popper(a_list)
    #packed = packer()
    #print(packed)
    #a_list = [1, 2, 3, 4, 5, 6]
    #swapped = swapper(a_list)
    #print(swapped)
    #a_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    #size = 2
    #chunky(a_list, size)
    #a_list = [7, 14, 21, 28, 35, 42, 49, 56, 63, 70, 77, 84, 91, 98]
    #lucky_7s(a_list)
    return

main()