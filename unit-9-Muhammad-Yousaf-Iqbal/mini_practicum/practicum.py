#Muhammad Yousaf Iqbal

def in_place_reverse(a_list):

    for (i) in range(len(a_list)):
        (x) = a_list.pop()
        a_list.insert(i, x)
    return (a_list)

def make_multiplication_table():

    return [[i * j for (j) in range(1, 11)] for (i) in range(1, 11)]

def main():

    print("Time Complexity: O(n^2) ??")
    original_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    print("Original List: ", original_list)
    reversed_list = in_place_reverse(original_list)
    print("Reversed List: ", reversed_list)
    print("Multiplication Table: ", make_multiplication_table())

main()

#Done