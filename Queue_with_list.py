class Queue:
    def __init__(self):
        self.queue=[]
        self.rear=None
        self.front=None

    def is_Empty(self):
        return len(self.queue) ==0