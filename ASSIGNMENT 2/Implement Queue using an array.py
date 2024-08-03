class Queue:
    def __init__(self):
        self.queue = []
    def enqueue(self, item):
        self.queue.append(item)
    def dequeue(self):
        return self.queue.pop(0) if not self.is_empty() else None
    def is_empty(self):
        return len(self.queue) == 0
q = Queue()
q.enqueue(1)
q.enqueue(2)
print(q.dequeue()) 