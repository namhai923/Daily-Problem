class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
    def preorder(self):
        print(self.value)
        if self.left: 
            self.left.preorder()
        if self.right:
            self.right.preorder()
def invert(node):
    if node.left:
        invert(node.left)
    if node.right:
        invert(node.right)
    node.left, node.right = node.right, node.left

root = Node('a')
root.left = Node('b')
root.right = Node('c')
root.left.left = Node('d')
root.left.right = Node('e')
root.right.left = Node('f')

root.preorder()
print("\n")
invert(root)
root.preorder()


        