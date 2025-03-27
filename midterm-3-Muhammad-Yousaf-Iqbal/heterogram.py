"""
A heterogram is a string in which no letter of the alphabet occurs more than
once.  Complete the function below to return True if the given string is a
heterogram and False otherwise.  As string with no letters should return False.
Notes:
 - The function should check only that letters occur once, so other characters.
   e.g. punctuation or numbers should be ignored.
 - Uppercase and lowercases letters are considered the same, e.g. "a" == "A"
Examples:
    is_heterogram("Computer")           # returns True--no duplicates
    is_heterogram("Jim asked 'wut?'")   # returns True--no duplicates
    is_heterogram("Testing 1-2-3!")     # returns False--T and t
    is_heterogram("1, 2, 3")            # returns False--no letters
You may update the main function below for the purposes of manual testing and
debugging.
"""
def is_heterogram(a_string):
    a_string = a_string.lower()
    if "a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t, u, v, w, x, y, z"  in a_string:
        return True
    if a_string == "":
        return False
    if "0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10" in a_string:
        return False
    if "a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t, u, v, w, x, y, z" and "A, B, C, D, E, F, G, H, I, J, K, L, M, N, O, P, Q, R, S, T, U, V, W, X, Y, Z" in a_string:
        return False
    else:
        return False
# For manual testing purposes, you may change as needed
def main():
    print(is_heterogram("Computer"))
    print(is_heterogram("Jim asked 'wut?'"))
    print(is_heterogram("Testing 1-2-3!"))
    print(is_heterogram("1, 2, 3"))
main()
#MYI
