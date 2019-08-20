class ListNode:
    def __init__(self, data):
        self.data = data
        self.next = None
    def change(self, a):
        a.data = 10

a = ListNode(5)
a.change(a)
print(a.data)