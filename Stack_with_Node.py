class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

class Stack:
    def __init__(self):
        self.stack=None
    
    def is_Empty(self):
        if self.stack is None:
            return True

    def push(self, val):
        data=Node(val)
        data.next=self.stack
        self.stack = data

    def pop(self):
        if self.is_Empty():
            raise IndexError("List is Empty")
        else:
            data=self.stack.data
            self.stack = self.stack.next
            return data
        
    def peek(self):
        if self.is_Empty():
            raise IndexError("List is Empty")
        return self.stack.data
    
    def length(self):
        num=0
        while self.stack is not None:
            num+=1
            self.stack = self.stack.next
        return num 
s=Stack()
s.push(9)
s.push(19)
s.push(89)
s.push(10)
print(s.peek())
s.pop()
print(s.peek())
print(s.length())