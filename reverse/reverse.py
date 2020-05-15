class Node:
    def __init__(self, value=None, next_node=None):
        self.value = value
        self.next_node = next_node

    def get_value(self):
        return self.value

    def get_next(self):
        return self.next_node

    def set_next(self, new_next):
        self.next_node = new_next

class LinkedList:
    def __init__(self):
        self.head = None

    def add_to_head(self, value):
        node = Node(value)

        if self.head is not None:
            node.set_next(self.head)

        self.head = node

    def contains(self, value):
        if not self.head:
            return False

        current = self.head

        while current:
            if current.get_value() == value:
                return True

            current = current.get_next()

        return False

    def reverse_list(self, node, prev):
        # here i used recursion.
        if node == None:
            return
        firstNode = node.get_next() # set first node to be recursive, after use the same variable
        #if the next node is none it is the end of and then we change it to head

        if not prev == None:
            node.set_next(prev)
        # recur
        # head is less than first node is less then node if itis none
        if not firstNode == None:
            self.reverse_list(firstNode, node)
        # set tail to new end
        else:
            self.head = node
