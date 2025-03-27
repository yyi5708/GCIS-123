import list_queue

def count_to_order(list_of_numbers:list) -> int:

    q = list_queue.Queue()
    print(q.enqueue(list_of_numbers))
    print(q.dequeue())
    print(q)
    print(q.enqueue())
    print(q)
    print(q.size())
    print(q)
    while not q.is_empty():
        print(q.dequeue())
    print(q.is_empty())
    print(q.size())
    print(q)
    return q.__repr__()

def main():

    a = [1, 2, 3, 4, 5]
    b = [5, 4, 3, 2, 1]
    c = [3, 1, 2]
    print(count_to_order(a))
    print(count_to_order(b))
    print(count_to_order(c))

if __name__ == '__main__':

    main()

