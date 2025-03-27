class Queue:

    __slots__ = ['__daqueue']

    def __init__(self) -> None:
        self.__daqueue = []

    def size(self):
        return len(self.__daqueue)

    def is_empty(self):
        return len(self.__daqueue) == 0

    def enqueue(self, value):
        self.__daqueue.append(value)

    def dequeue(self):
        return self.__daqueue.pop(0)

    def peek(self, back = False):
        if back:
            return self.__daqueue[len(self.__daqueue)-1]
        else:
            return self.__daqueue[0]

    def __repr__(self) -> str:
        return repr(self.__daqueue)

def main():

    q = Queue()
    print(q.is_empty())
    print(q.size())
    print(q)
    for i in range(5):
        q.enqueue(i)
        print(q.peek(), q.peek(True))
    print(q.is_empty())
    print(q.size())
    print(q)
    while not q.is_empty():
        print(q.dequeue())
    print(q.is_empty())
    print(q.size())
    print(q)

if __name__ == '__main__':

    main()

