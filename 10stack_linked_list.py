class Node:
    
    def __init__(self,item=None,next=None):
        self.item=item
        self.next=next
    
class stack:
    
    def __init__(self,start=None,count=0) -> None:
        self.start=start
        self.count=count
    def push(self,data):
        nn=Node(data)
        if self.start==None:
            self.start=nn
            self.count+=1
        else:
            t=self.start
            while t.next!=None:
                t=t.next
            t.next=nn
            self.count+=1
    def is_empty(self):
        return self.start==None
    def number_of_nodes(self):
        if not self.is_empty():
            return self.count
        print("the stack is empty")

    def pop(self):
        if not self.is_empty():
            t1=self.start
            t2=self.start.next
            while t2.next!=None:
                t1=t1.next
                t2=t2.next
            t1.next=None
            self.count-=1

    def peek(self):
        if not self.is_empty():
            t=self.start
            while t.next!=None:
                t=t.next
            print(t.item)
s1=stack()
s1.push(23)
s1.push(3)
s1.push(2)
s1.push(6)
s1.peek()
s1.pop()
s1.peek()
