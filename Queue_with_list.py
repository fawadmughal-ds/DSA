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
    