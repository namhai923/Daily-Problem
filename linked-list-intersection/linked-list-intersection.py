def intersection(a, b):
    node_set = set()
    while a:
        node_set.add(a)
        a = a.next
    while b:
        if b in node_set:
            return b
        b = b.next

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def prettyPrint(self):
        c = self
        while c:
            print(c.value)
            c = c.next

a = Node(1)
a.next = Node(2)
a.next.next = Node(3)
a.next.next.next = Node(4)

b = Node(6)
b.next = a.next.next

c = intersection(a, b)
c.prettyPrint()
