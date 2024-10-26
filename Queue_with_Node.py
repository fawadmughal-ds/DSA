class Node:
    def __init__(self,data):
        self.data= data
        self.next = None

class Queue:
    def __init__(self):
        self.front = None
        self.rear = None
        self.item_count=0

    def is_Empty(self):
        return self.front is None

    def Enqueue(self,val):
        data=Node(val)
        if self.is_Empty():
            self.front=data
        else:
            self.rear.next=data
        self.rear = data
        self.item_count +=1

    def Dequeue(self):
        if self.is_Empty():
            raise IndexError("Queue is Empty")
        elif self.rear == self.front:
            self.front = None
            self.rear = None
        else:
            self.front =self.front.next
        self.item_count -=1

    def get_front(self):
        if self.is_Empty():
            raise IndexError("List is Empty")
        return self.front.data
    
    def get_rear(self):
        if self .is_Empty():
            raise IndexError("List is Empty")
        return self.rear.data
    
    def length(self):
        return self.item_count
    

q=Queue()
q.Enqueue(9)
q.Enqueue(19)
q.Enqueue(89)
q.Enqueue(10)
print(q.get_front())
q.Dequeue()
print(q.get_rear())
print(q.get_front())
print(q.length())
