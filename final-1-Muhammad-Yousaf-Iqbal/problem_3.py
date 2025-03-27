import list_stack

def item_buffer(items:list) -> list:

    s = list_stack.Stack()
    LIFO_buffer = []
    result_list = []
    while items is not s.is_empty():
        x = (s.pop(items))
        LIFO_buffer.append(x)
        y = LIFO_buffer.pop()
        result_list.append(y)
        return LIFO_buffer and result_list

def main():

    x = item_buffer([1, 2, 3])
    print(x)
    y = item_buffer(['one', 'two', 'three', 'four'])
    print(y)

if __name__ == '__main__':

    main()

