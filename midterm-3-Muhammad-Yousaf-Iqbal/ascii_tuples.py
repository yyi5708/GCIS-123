"""
This questions has two parts: A and B.
You have been provided with unit tests for each part in ascii_tuples_test.py.
Do not alter any of the tests.  All tests should pass for your solution to be
complete.
You may update the main function below for the purposes of manual testing and
debugging.
"""
"""
Part A: Given a list of words, complete the function below to return a list
of tuples, where the elements of each tuple are the ascii values of the letters
of each word.
Bonus (5 pts): write your solution in one line
Example:
  make_ascii_tuples(["dog","car","it","cake"])
  # returns [(100, 111, 103), (99, 97, 114), (105, 116), (99, 97, 107, 101)]
"""
def make_ascii_tuples(word_list):
    x = []
    for word in word_list:
        for char in word:
            y = tuple(ord(char))
            x.append(y)
    return x
"""
Part B: Complete the function below to sort the list of tuples of with ascii
values, in increasing order, based on the sum of the ascii values for each
tuple.
The function must be non-destructive, i.e. returns a new list with the tuples
in sorted order.  The ordering of the original list should remain unchanged.
Example:
    sort_ascii_tuples([(100, 111, 103), (99, 97, 114), (105, 116), (99, 97, 107, 101)])
    # returns [(105, 116), (99, 97, 114), (100, 111, 103), (99, 97, 107, 101)]
"""
def sort_ascii_tuples(ascii_tuple_list):
    x = sum(ascii_tuple_list)
    sort = sorted(ascii_tuple_list, x)
    return sort
# For manual testing purposes, you may change as needed
def main():
    word_list = ["dog","car","it","cake"]
    ascii_tuple_list = make_ascii_tuples(word_list)
    print("Ascii Tuples:",ascii_tuple_list)
    sorted_ascii_tuple_list = sort_ascii_tuples(ascii_tuple_list)
    print("Sorted Ascii Tuples:",sorted_ascii_tuple_list)
if __name__ == "__main__":
    main()
#MYI
