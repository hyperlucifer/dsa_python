class Node:
    def __init__(self,data=None,next=None) -> None:
        self.data=data
        self.next=next
    
class dequeue:
    def __init__(self,start=None) -> None:
        self.start=start

    def is_empty(self):
        return self.start==None
    def insert_frount(self,data):
        nn=Node(data)
        if self.is_empty():
            self.start=nn
        else:
            nn.next=self.start
            self.start=nn

    def insert_last(self,data):
        nn=Node(data)
        if self.is_empty():
            self.insert_last(data)
        else:
            t=self.start
            while t.next!=None:
                t=t.next
            t.next=nn            

    def delete_first(self):
        if self.is_empty():
            print("list is empty")
            return
        else:
            self.start=self.start.next
    
    def delete_last(self):
        if self.is_empty():
            print("list is empty")
            return
        else:
            t=self.start
            t1=self.start.next
            while t1.next!=None:
                t=t.next
                t1=t1.next
            t.next=None
    
    def display_first(self):
        if self.is_empty():
            print("list is empty")
            return
        else:
            print(self.start.data)
    
    def display_last(self):
        if self.is_empty():
            print("list is empty")
            return
        else:
            t=self.start
            while t.next!=None:
                t=t.next
            print(t.data)

dq=dequeue()

dq.insert_frount(32)
dq.insert_frount(3)
dq.insert_last(6666)
dq.display_last()