class Node:
    def __init__(self, val, next = None):
        self.val = val
        self.next = next
    
    def __str__(self):
        c = self
        answer = ""
        while c:
            answer += str(c.val) if c.val else ""
            c = c.next
        return answer

def merge(lists):
    list_result = []
    result = None
    while lists:
        lists = sorted(lists, key = lambda i: i.val)
        list_result.append(lists[0].val)
        lists[0] = lists[0].next
        if lists[0] is None:
            lists.remove(lists[0])
    for i in range(len(list_result)-1, 0-1, -1):
        temp = result
        result = Node(list_result[i], temp)
    return result

a = Node(1, Node(3, Node(5)))
b = Node(2, Node(4, Node(6)))
print(merge([a,b]))