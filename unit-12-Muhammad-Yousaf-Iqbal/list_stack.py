#MYI

class Stack:

    def __init__(self):

        (self.list_stack) = ([])

    def push(self, item):

        (self.list_stack.append(item))

    def pop(self):

        return(self.list_stack.pop())

    def peek(self):
    
        return(self.list_stack[-1])

    def is_empty(self):
    
        return(len(self.list_stack) == 0)

    def __repr__(self):

        return(f"{self.list_stack[::-1]}")

def main():

    pass

if __name__ == "__main__":

    main()

#Done
