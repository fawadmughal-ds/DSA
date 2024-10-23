class Stack:
    def __init__(self):
        self.stack=[]

    def is_Emtpy(self):
        return len(self.stack)==0
    
    def push(self, val):
        self.stack.append(val)

    def pop(self):
        if self.is_Emtpy is None:
            raise IndexError("List is Empty")
        self.stack.pop()
    
    def peek(self):
        if self.is_Emtpy is None:
            raise IndexError("List is Empty")
        return self.stack[-1]
    
    def length(self):
        return len(self.stack)
    

s=Stack()
s.push(9)
s.push(19)
s.push(89)
s.push(10)
print(s.peek())
s.pop()
print(s.peek())
print(s.length())
