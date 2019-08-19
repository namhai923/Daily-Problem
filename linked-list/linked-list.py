class ListNode:
    def __init__(self, data):
        self.data = data
        self.next = None

class Solution:

    def addTwoNumbers(self, l1, l2, c = 0):
        root = None
        num1 = self.toNumber(l1)
        num2 = self.toNumber(l2)
        lresult = num1 + num2
        lresult = list(str(lresult))
        for digit in lresult:
            new_node = ListNode(int(digit))
            new_node.next = root
            root = new_node
        return root

    def toNumber(self, l1):
        number_result = 0
        counter = 1
        while l1:
            number_result += l1.data*counter
            l1 = l1.next
            counter *= 10
        return number_result
 
l1 = ListNode(2)
l1.next = ListNode(4)
l1.next.next = ListNode(3)

l2 = ListNode(5)
l2.next = ListNode(6)
l2.next.next = ListNode(4)

result = Solution().addTwoNumbers(l1,l2)
while result:
    print(result.data)
    result = result.next
