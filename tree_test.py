class Node:
    def __init__(self, value):
        self.left = None
        self.right = None
        self.value = value
    
    def insert_node(self, value):
        if value <= self.value:
            if self.left is None:
                self.left = Node(value)
            else:
                self.left.insert_node(value)
        else:
            if self.right is None:
                self.right = Node(value)
            else:
                self.right.insert_node(value)
    
    def contains_value(self, value):
        if value == self.value:
            return True
        elif value < self.value:
            if self.left is None:
                return False
            else:
                return self.left.contains_value(value)
        else:
            if self.right is None:
                return False
            else:
                return self.right.contains_value(value)
    
    def print_in_order(self):
        if self.left:
            self.left.print_in_order()
        print(self.value, ' ', end='')
        if self.right:
            self.right.print_in_order()

root = Node(18)
root.insert_node(14)
root.insert_node(39)
root.insert_node(10)
root.insert_node(17)
root.insert_node(27)
root.insert_node(40)

root.print_in_order()
val = 19
print("{} that tree contains {}".format(root.contains_value(val), val))