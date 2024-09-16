class Node:
    def __init__(self,data=None,next=None) -> None:
        self.data=data
        self.next=next

class queue:
    def __init__(self,start=None) -> None:
        self.start=start

    def insert(self,data):
        nn=Node(data)
        if self.start==None:
            self.start=nn
        else:
            t=self.start
            while t.next!=None:
                t=t.next
            t.next=nn
    
    def is_empty(self):
        return self.start==None
    def pop(self):
        if not self.is_empty():
            self.start=self.start.next

    def peek(self):
        if not self.is_empty():
        
            return self.start.data
        
q=queue()
q.insert(23)
q.insert(4)
q.insert(3)
q.insert(2)
q.insert(7)
print(q.peek())
q.pop()
print(q.peek())