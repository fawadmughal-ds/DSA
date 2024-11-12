class Node:
    def __init__(self, val=None):
        self.info = val
        self.next = None
        self.prev = None

class LinkList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert_at_head(self, val):
        new_node = Node(val)
        if self.head is None:
            self.head= new_node
            self.tail = new_node
        else:
            new_node.next= self.head
            self.head = new_node
        
    def insert_at_tail(self, val):
        new_node = Node(val)
        if self.tail is None:
            self.head= new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node

    def insert_after(self,key,val):
        new_node= Node(val)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            temp = self.head
            while temp:
                if temp.info == key:
                    new_node.prev = temp
                    new_node.next = temp.next
                    temp.next = new_node
                    if temp.next:
                        temp.next.prev= new_node
                    else:
                        self.tail = new_node
                    return
                temp =temp.next


    def insert_before(self,key,val):
        pass

    def remove_from_head(self):
        if self.head is None:
            raise ValueError("This Linked has not head")
        temp = self.head
        self.head = temp.next 
        del temp 

    def remove_from_tail(self):
        if self.tail is None:
            raise ValueError("This LinkedList Has not Tail")
        temp = self.tail 
        self.tail = temp.prev
        self.tail.next= None
        del temp 

    def remove_after(self,key):
        if self.tail is None:
            raise ValueError("This LinkedList Has not Tail")
        else:
            temp1 = self.head
            temp2 = self.head.next
            while temp2.info == key:
                temp2.next = temp1
                temp2.next.prev= temp1
            del temp2

    def remove_before(self,key):
        pass
        
    def update(self, key,val):
        pass

    def Search(self, key):
        pass

    def display(self):
        pass
        temp=self.head
        while temp is not None:
            print(temp.info,end='-->')
            temp=temp.next

def main():
        if __name__ == "__main__":
            obj = LinkList()
            obj.insert_at_head(2)
            obj.insert_at_head(3)
            obj.insert_at_head(4)
            obj.insert_at_head(5)
            obj.insert_at_tail(10)
            obj.insert_at_tail(9)
            obj.insert_at_tail(8)
            obj.insert_at_tail(7)
            obj.insert_after(9,13)
#         obj.insert_before(3,62)
            obj.remove_from_head()
            obj.remove_from_tail()
            obj.remove_after(10)
#         obj.remove_before(8)
#         obj.update(62,100)
#         obj.Search(2)
            obj.display()
main()