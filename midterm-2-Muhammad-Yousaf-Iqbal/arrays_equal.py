"""
Complete the function below to determine if the given arrays are equal.

Two arrays are considered equal if they have the same number of elements, and
the value of the elements at the corresponding index of each array are equal.
That is the same elements appear in the exact same order in each array.

*** Your solution must be recursive.  You can add parameters with default values
as needed.  ***

The function returns True if the arrays are equal, False otherwise

Examples:
    arrays_equal( [], [] )           # True
    arrays_equal( [1], [1] )         # True
    arrays_equal( [1,2], [2,1] )     # False
    arrays_equal( [1,2,3], [1,2] )   # False
    arrays_equal( [1,2,3], [1,2,3] ) # True

You have been provided with unit tests in arrays_equal.py.  Do not alter any
of the tests.  All tests should pass for your solution to be complete.
"""

def arrays_equal(array1,array2,index=0):
    if array1 == array2:
        return(True)
    if index in range(array1) == index in range (array2):
        return(True)
    if array1 != array2:
        return(False)
    if index in range(array1) != index in range (array2):
        return(False)
    if [0] in array1 == [0] in array2:
        return(True)
    if [0] in array1 != [0] in array2:
        return(False)
    if [1] in array1 == [1] in array2:
        return(True)
    if [1] in array1 != [1] in array2:
        return(False)
    else:
        arrays_equal(array1, array2, index=0)
    
#Done