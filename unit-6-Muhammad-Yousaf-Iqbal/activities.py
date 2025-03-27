import arrays
import random
import time
import searches
import turtle
import math

def making_arrays():
    s_5 = arrays.Array(5, None)
    print(s_5)
    s_1 = arrays.Array(1, 0)
    print(s_1)
    s_10 = arrays.Array(10, "")
    print(s_10)
    s_20 = arrays.Array(20, False)
    print(s_20)

def while_fill(an_array):
    print("Before:", an_array)
    length = len(an_array)
    counter = 0
    while counter < length:
        an_array[counter] = counter * 2
        counter += 1
    print("After:", an_array)

def for_fil(an_array):
    print("Before:", an_array)
    length = len(an_array)
    counter = 0
    for index in range(length):
        print("After:", an_array[index])    

def roll_the_dice(sides):
    return random.randint(1, sides)

def linear_search_timer(an_array, target):    
    begin = time.perf_counter()
    searches.linear_search(an_array, target)
    end = time.perf_counter()
    elapsed = end - begin
    return elapsed

def print_odds(an_array):

    length = len(an_array)
    for index in range(length):
        value = an_array[index]
        if value % 2 != 0:
            print(value, end="")
        print()

def print_odds_rec(an_array, index=0):

    length = len(an_array)
    for index in range(length):
        value = an_array[index]
        if value % 2 != 0:
            print(value, end="")
        if index >= len(an_array):
            print_odds_rec(an_array,index+1)
        else:
            return

def factorial(N):
    if N < 0:
        return None
    if N == 0:
        return 1
    if N == 1:
        return 1
    else:
       fact_rest = factorial (N - 1)
       return N * fact_rest

def main():
    #making_arrays()
    #x = arrays.Array(10)
    #while_fill(x)
    #for_fil(x)
    #random.seed(1)
    #counter = 0
    #while counter != 10:
        #x = roll_the_dice(6)
        #print("Rolling A Six Sided Die:",x)
        #counter += 1
    #array_a = array_utils.range_array(1,10000000)
    #print("1:", linear_search_timer(array_a, 1))
    #print("5000000:", linear_search_timer(array_a, 5000000))
    #print("10000000:", linear_search_timer(array_a, 10000000))
    #array_a = array_utils.range_array(0,100)
    #print_odds(array_a)
    #array_a = array_utils.range_array(0, 10)
    #print_odds_rec(array_a)
    #print(factorial(10))
    #print(factorial(100))
    #print(factorial(2000))
    return

if __name__ == "__main__":
    main()
