class Node:

    __slots__ = ['__value', '__next']

    def __init__(self, value, next = None) -> None:
        self.__value = value
        self.__next = next

    def get_value(self):
        return self.__value

    def get_next(self):
        return self.__next    
    
    def set_next(self, next_node):
        self.__next = next_node
    
def print_node(node_seq:Node):

    if node_seq == None:
        print(end = '')
    else:
        print(node_seq.get_value(), end = ', ')
        print_node(node_seq.get_next())

def main():

    node1 = Node(1, None)
    node2 = Node(2, node1)
    node3 = Node(3, node2)
    print_node(node3)

if __name__ == '__main__':

    main()

