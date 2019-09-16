class Queue:
    def __init__(self):
        self.queue = []
    def enqueue(self,val):
        self.queue.insert(0, val)
    def dequeue(self):
        return self.queue.pop()
        
q = Queue()
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)
print(q.dequeue())
print(q.dequeue())
print(q.dequeue())