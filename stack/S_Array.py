class Stack:
    def __init__(self):
        self.s = []

    def length(self):
        return len(self.s)
    
    def is_empty(self):
        return self.length() == 0
    
    def push(self, value):
        self.s.insert(0, value)
    
    def pop(self):
        if self.is_empty():
            raise Exception("Stack is empty")
        return self.s.pop(0)
    
    def peek(self):
        if self.is_empty():
            raise Exception("Stack is empty")
        return self.s[0]
    
    def __str__(self):
        return str(self.s)


st = Stack()
st.push(10)
st.push(29)
st.push(22)

print(st)        # [22, 29, 10]
print(st.pop())  # 22
print(st.peek()) # 29