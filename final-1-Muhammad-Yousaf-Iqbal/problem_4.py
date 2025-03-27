import node

class OrderedNodeSequence():

    __slots__ = ['__firstNode']

    def __init__(self) -> None:

        self.__firstNode = None

    def insert(self, value):
        
        new_node = node.Node(value)
        if self.__firstNode == None:
            self.__firstNode = new_node
        else:
            inserted = False
            insert_spot = self.__firstNode
            previous_spot = None
            while not inserted:
                if insert_spot.get_value() > value:
                    if insert_spot == self.__firstNode:
                        self.__firstNode = new_node
                    else:
                        previous_spot.set_next(new_node)
                    new_node.set_next(insert_spot)
                    inserted = True
                else:
                    if insert_spot.get_next() == None:
                        insert_spot.set_next(new_node)
                        inserted = True
                    else:
                        previous_spot = insert_spot
                        insert_spot = insert_spot.get_next()

    def __repr__(self) -> str:
    
        return self.__firstNode

    def is_empty(self) -> bool:
    
        if node.Node() == (""):
            return True
        else:
            return False

    def peek(self):

        if OrderedNodeSequence() == []:
            return None
        else:
            return self.__firstNode()
    
    def contains(self, value) -> bool:
    
        if OrderedNodeSequence == value:
            return True
        else:
            return False
        
    def remove(self, value) -> bool:
    
        OrderedNodeSequence.__firstNode.set_next(value)
        if value in OrderedNodeSequence:
            return True
        else:
            return False

def main():

    return

if __name__ == '__main__':

    main()

