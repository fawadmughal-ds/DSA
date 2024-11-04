class Node:
    def __init__(self, val=None):
        self.info = val
        self.next = None

class LinkList:
    def __init__(self):
        self.head = None

    def insert_at_head(self, val):
        new_node=Node(val)
        if self.head is None:
            self.head=new_node
        else:
            new_node.next=self.head
            self.head= new_node
        
    def insert_at_tail(self, val):
        new_node=Node(val)
        if self.head is None:
            self.head= new_node
        else:
            temp=self.head
            while temp.next is not None:
                temp=temp.next
            temp.next =new_node

    def insert_after(self,key,val):
        new_node= Node(val)
        if self.head is None:
            raise ValueError("LinkedList is Empty ")
        else:
            temp=self.head
            while temp:
                if temp.info == key:
                    new_node.next=temp.next
                    temp.next=new_node
                    return
                temp=temp.next
            raise ValueError("No Value find")
        
    def insert_before(self,key,val):
        new_node=Node(val)
        if self.head is None:
            self.head = new_node
        else:
            temp = self.head
            while temp:
                if temp.next.info == key:  
                    new_node = Node(val)
                    new_node.next = temp.next
                    temp.next = new_node
                    return
                temp = temp.next

    def remove_from_head(self):
        if self.head is None : 
           raise ValueError('No Element Exists')
        temp=self.head
        self.head=self.head.next
        del temp

    def remove_from_tail(self):
        if self.head is None:
            raise ValueError('No Element Exists')
        if self.head.next is None:
            self.head = None
            return
        temp1=self.head
        temp2=self.head.next
        while temp2.next is not None:
            temp1 = temp1.next
            temp2= temp2.next
        del temp2
        temp1.next=None

    def remove_after(self,key):
        if self.head is None:
            raise ValueError("LinkedList is Empty ")
        temp1=self.head
        temp2=self.head.next
        while temp2.info == key:
            temp1 = temp1.next
            temp2= temp2.next
        del temp2
        temp1.next=temp1.next.next

    def remove_before(self,key):
        if self.head is None or self.head.next is None:
            raise ValueError("LinkedList is Empty or has only one element")
        if self.head.info == key:
            raise ValueError("No node before the head")
        if self.head.next.info == key:
            self.remove_from_head()
            return
        temp1=self.head
        temp2=self.head.next
        while temp2.info == key:
        
            del temp2
        temp1 = temp1.next.next

    def remove(self, val):
        if self.head is None:
            raise ValueError("LinkedList is Empty")
        if self.head.info == val:
            self.head = self.head.next
            return
        prev = None
        temp = self.head
        while temp:
            if temp.info == val:
                prev.next = temp.next
                del temp
                return
            prev = temp
            temp = temp.next
        
        raise ValueError("Value not found in the LinkedList")


    def update(self, key,val):
        temp=self.head
        while temp.info != key:
            temp.next.info=val
            return
    def Search(self, key):
        temp=self.head
        while temp:
            if temp.info == key:
                return temp
            temp = temp.next

    def display(self):
        temp=self.head
        while temp is not None:
            print(temp.info,end='-->')
            temp=temp.next


def main():
    if __name__ == "__main__":
        obj = LinkList()
        obj.insert_at_head(2)
        obj.insert_at_head(2)
        obj.insert_at_head(3)
        obj.insert_at_head(4)
        obj.insert_at_head(5)
        obj.insert_at_tail(10)
        obj.insert_at_tail(9)
        obj.insert_at_tail(8)
        obj.insert_at_tail(8)
        obj.insert_at_tail(8)
        obj.insert_at_tail(7)
        obj.insert_after(8,13)
        obj.insert_before(3,62)
        obj.remove_from_head()
        obj.remove_from_tail()
        obj.remove_before(8)
        obj.update(62,100)
        obj.Search(2)
        obj.remove(8)
        obj.display()
main()
