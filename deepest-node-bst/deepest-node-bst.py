class Node(object):
    def __init__(self, value, left = None, right = None):
        self.value = value
        self.left = left
        self.right = right
    def __repr__(self):
        return self.value

def deepest(node):
    left_count = 1
    right_count = 1
    if node.left or node.right:
        if node.left:
            left_count += deepest(node.left)[1]
        if node.right:
            right_count += deepest(node.right)[1]
        if left_count >= right_count:
            node.value = node.left.value
        else:
            node.value = node.right.value
    else:
        return '', max(left_count, right_count)
    return node.value, max(left_count, right_count)

root = Node('a')
root.left = Node('b')
root.left.left = Node('d')
root.right = Node('c')

print(deepest(root))