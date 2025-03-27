class Node:

    __slots__ = ["__value", "__next"]

    def __init__(self, value, next = None):

        self.__value == value
        self.__next == next
    
    def get_value(self):

        return self.__value
    
    def get_next(self):

        return self.__next
    
def print_node(node_seq):

    if node_seq == None:
        print("")
    else:
        print(node_seq.get_value(), end = ", ")
        print_node(node_seq.get_next())

def main():

    node_1 = Node("a", node_1)
    node_2 = Node("b", node_2)
    node_3 = Node("c", node_3)
    node_4 = Node("d", node_4)
    node_5 = Node("e", node_5)
    node_6 = Node("f", node_6)
    print_node(node_1)
    print_node(node_2)
    print_node(node_3)
    print_node(node_4)
    print_node(node_5)
    print_node(node_6)

if __name__ == "__main__":

    main()
