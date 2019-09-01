class Node:
    def __init__(self, value):
        self.value = value
        self.right = None
        self.left = None
    
def findCeilingFloor(root, key, floor = None, ceil = None):
    if(key == root.value):
        ceil = root.value
        floor = root.value
        return floor, ceil
    if(key > root.value):
        if root.right:
            floor = root.value
            root = root.right
            result = findCeilingFloor(root, key, floor, ceil)
        else:
            floor = root.value
            return floor, ceil
    if (key < root.value):
        if root.left:
            ceil = root.value
            root = root.left
            result = findCeilingFloor(root, key, floor, ceil)      
        else:
            ceil = root.value
            return floor, ceil
    return result

root = Node(8)
root.right = Node(12)
root.left = Node(4)

root.left.left = Node(2)
root.left.right = Node(6)

root.right.left = Node(10)
root.right.right = Node(14)

print(findCeilingFloor(root,8))