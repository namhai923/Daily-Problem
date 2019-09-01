class Node:
    def __init__(self, value, next = None):
        self.val = value
        self.next = next

def removeConsecutiveSumTo0(node):
    prev = None
    start = node
    while start:
        end = start
        result = 0
        while end:
            result += end.val
            if result == 0:
                if prev:
                    prev.next = end.next
                    start = prev
                    end.next = None
                else:
                    start = end.next
                    node = end.next
                    end.next = None
            end = end.next
        if result != 0:
            prev = start
            start = start.next
    return node


node = Node(10)
node.next = Node(5)
node.next.next = Node(-3)
node.next.next.next = Node(-3)
node.next.next.next.next = Node(1)
node.next.next.next.next.next = Node(4)
node.next.next.next.next.next.next = Node(-4)
node = removeConsecutiveSumTo0(node)
while node:
    print(node.val)
    node = node.next   