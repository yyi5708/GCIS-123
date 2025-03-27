"""
Complete the function below to return a list of unique elements in the given
sequence.
Examples:
    unique_elements("aardvark")               # returns ['d', 'a', 'v', 'r', 'k']
    unique_elements([1, 4, 0, 3, 0, 4, 8, 1]) # returns [0, 1, 3, 4, 8]
Note: that the ordering of elements within the returned list does not matter.
You have been provided with unit tests in unique_letters_test.py.  Do not alter
any of the tests.  All tests should pass for your solution to be complete.
You may update the main function below for the purposes of manual testing and
debugging.
"""
def unique_elements(a_sequence):
    a_list = []
    if a_sequence == "":
        return []
    a_set = set()
    for i in a_sequence:
        a_set.add(i)
        a_list = list(a_set)
    return a_list
# For manual testing purposes, you may change as needed
def main():
    print(unique_elements("aardvark"))
    print(unique_elements([1, 4, 0, 3, 0, 4, 8, 1]))
if __name__ == "__main__":
    main()
#MYI
