class MaxStack:
    def __init__(self):
        self.data = []
    def push(self, val):
        self.data.append(val)
    def pop(self):
        self.data.pop()
    def max(self):
        if len(self.data) == 0:
            return None
        return max(self.data)

s = MaxStack()
s.push(1)
s.push(2)
s.push(3)
s.push(2)
print(s.max())
s.pop()
s.pop()
print(s.max())