class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None
  
    def printList(self):
        node = self
        output = '' 
        while node != None:
            output += str(node.val)
            output += " "
            node = node.next
        print(output)


    def reverseIteratively(self):
        prev = None
        while self:
            next = self.next
            self.next = prev
            prev = self
            self = next
  
    # def reverseRecursively(self, head):
        

testHead = ListNode(4)
node1 = ListNode(3)
testHead.next = node1
node2 = ListNode(2)
node1.next = node2
node3 = ListNode(1)
node2.next = node3
testTail = ListNode(0)
node3.next = testTail

print("Initial list: ")
testHead.printList()
testHead.reverseIteratively()
print("List after reversal: ")
testTail.printList()
