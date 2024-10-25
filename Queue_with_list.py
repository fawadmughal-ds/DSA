class Queue:
    def __init__(self):
        self.queue=[]
        self.rear=None
        self.front=None

    def is_Empty(self):
        return len(self.queue) ==0
    
    def Enqueue(self,val):
        self.queue.append(val)

    def Dequeue(self):
        if self.is_Empty() is None:
            raise IndexError("List is Empty")
        self.queue.pop(0)

    def get_front(self):
        if self.is_Empty() is None:
            raise IndexError("List is Empty")
        return self.queue[0]
    
    def get_rear(self):
        if self .is_Empty() is None:
            raise IndexError("List is Empty")
        return self.queue[-1]
    
    def length(self):
        return len(self.queue)
    

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