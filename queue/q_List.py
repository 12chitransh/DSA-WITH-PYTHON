class Queue:
    def __init__(self):
        self.item = []

    def is_empty(self):
        return len(self.item) == 0
    
    def insert(self, value):
        self.item.append(value)
    
    def pop(self):
        if self.is_empty():
            raise Exception("Queue is empty")
        return self.item.pop(0)
    
    def __str__(self):
        return str(self.item)


# Usage
q = Queue()
q.insert(12)
q.insert(23)
q.insert(56)

q.pop()

print(q)   # [23, 56]