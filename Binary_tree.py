class Node(object):
    def __init__(self):
        self.value = None
        self.left = None
        self.right = None

    node0 = Node("Apple")
    node0.value
    node0.right
    node0.left

    def set_Value(self, new_value):
        self.value = new_value

    def get_value(self):
        self.value

    print(node0.value)
