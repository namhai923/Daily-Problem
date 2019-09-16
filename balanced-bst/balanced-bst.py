from collections import deque

class Node:
    def __init__(self, value, left = None, right = None):
        self.value = value
        self.left = left
        self.right = right

    def __str__(self):
        nodes = deque([self])
        answer = ''
        while len(nodes):
            node = nodes.popleft()
            if not node:
                continue
            answer += str(node.value)
            nodes.append(node.left)
            nodes.append(node.right)
        return answer

def createBalancedBST(nums):
    if nums:
        root = Node(nums[int((len(nums)-1)/2)])
        root.left = createBalancedBST(nums[:int((len(nums)-1)/2)])
        root.right = createBalancedBST(nums[int((len(nums)-1)/2+1):])
    else:
        return
    return root

print(createBalancedBST([1,2,3,4,5,6,7]))

    