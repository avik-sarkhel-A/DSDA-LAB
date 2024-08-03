class Stack:
    def __init__(self):
        self.stack = []
    def push(self, item):
        self.stack.append(item)
    def pop(self):
      return self.stack.pop() if not self.is_empty() else None
    def is_empty(self):
        return len(self.stack) == 0
s = Stack()
s.push(1)
s.push(2)
print(s.pop())  