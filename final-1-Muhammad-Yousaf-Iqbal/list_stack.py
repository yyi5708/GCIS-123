import node

class Stack:

    __slots__ = ['__stack']

    def __init__(self) -> None:
        self.__stack = []
    
    def push(self, value):
        self.__stack.append(value)

    def peek(self):
        return self.__stack[len(self.__stack)-1]
    
    def pop(self):
         return self.__stack.pop()

    def get_size(self):
        return len(self.__stack)
    
    def is_empty(self):
        return len(self.__stack) == 0
  
    def __repr__(self) -> str:
        return str(self.__stack)
    
def main():

    stack = Stack()
    print(stack.is_empty())
    for i in range(3):
        stack.push(i)
        print(stack.peek())
    print(stack)
    print(stack.get_size())
    print(stack.is_empty())
    print(stack.peek())
    print('Empty the stack')
    while not stack.is_empty():
        print(stack.pop())

if __name__ == '__main__':

    main()

