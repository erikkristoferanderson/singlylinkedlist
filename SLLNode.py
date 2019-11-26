class SLLNode:
    """
    A node in a singly linked list.
    Attributes:
        value - the value to be stored and displayed, integer
        next - a reference to the next Node in the list
    """

    def __init__(self, value=None, next_node=None):
        self.value = value
        self.next_node = next_node

    def __str__(self):
        s = "Node with value {} and ".format(self.value)
        if not self.next_node:
            s += "no next node"
        else:
            s += "next node has value {}.".format(self.next_node.value)
        return s


# testing it
if __name__ == "__main__":
    node = SLLNode(7, None)
    print()
    print(node)

    my_node = SLLNode(8, None)
    print(my_node)

    second_node = SLLNode(27, None)
    first_node = SLLNode(14, second_node)
    print(first_node)