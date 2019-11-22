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
        s = "Node with value {} and next node {}.".format(self.value, self.next_node)
        return s


# testing it
if __name__ == "__main__":
    node = SLLNode(7, None)
    print()
    print(node)
