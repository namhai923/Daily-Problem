class Node:
    def __init__(self, value, next = None):
        self.val = value
        self.next = next
    def __str__(self):
        current_node = self
        result = []
        while current_node:
            result.append(current_node.val)
            current_node = current_node.next
        return str(result)

def remove_kth_from_linked_list(head, k):
    remove_node = head
    prev = None
    if k == 1:
        head = head.next
    else:
        for _ in range(0, k-1):
            prev = remove_node
            remove_node = remove_node.next
        prev.next = remove_node.next
        remove_node.next = None
    return head

head = Node(1, Node(2, Node(3, Node(4, Node(5)))))
print(head)
head = remove_kth_from_linked_list(head, 3)
print(head)