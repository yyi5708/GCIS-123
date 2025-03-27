#MYI

from list_stack import Stack

def test_push():

    #setup
    (list_stack) = (Stack())
    #invoke
    (list_stack.push(1))
    (list_stack.push(2))
    (list_stack.push(3))
    (list_stack.push(4))
    #analyze
    assert(list_stack.peek() == 4)

def test_pop():
    
    #setup
    (list_stack) = (Stack())
    #invoke
    (list_stack.push(1))
    (list_stack.push(2))
    (list_stack.push(3))
    (list_stack.push(4))
    #analyze
    assert(list_stack.pop() == 4)
    assert(list_stack.pop() == 3)
    assert(list_stack.pop() == 2)
    assert(list_stack.pop() == 1)

def test_peek():

    #setup
    (list_stack) = (Stack())
    #invoke
    (list_stack.push(1))
    (list_stack.push(2))
    (list_stack.push(3))
    (list_stack.push(4))
    #analyze
    assert(list_stack.peek() == 4)

def test_is_empty():

    #setup
    (list_stack) = (Stack())
    #invoke
    pass
    #analyze
    assert(list_stack.is_empty() == True)

def test_repr():

    #setup
    (list_stack) = (Stack())
    #analyze
    (list_stack.push(1))
    (list_stack.push(2))
    (list_stack.push(3))
    (list_stack.push(4))
    #invoke
    assert(repr(list_stack) == "[4, 3, 2, 1]")

def main():

    pass

if __name__ == "__main__":

    main()

#Done
