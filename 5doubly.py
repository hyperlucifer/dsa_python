'''
Limitations of sll......
it contains the referance of the previous node too
that's why we can traverce forward and back words
Doubly Linked List......
doubly linled list is a liner data structure 
it constist of 3 variables prev, item, next 
the next of the last node consist none
the prev of the first node consist none
it needs more memory than singly linked list

operations ........
1)insertion
2)deletion
3)traversing
4)searching
5)is_empty
'''
class Node:
    def __init__(self,item=None,prev=None,next=None) :
        self.prev=prev
        self.item=item
        self.next=next

class dll:
    def __init__(self,start=None):
        self.start=start
    def is_empty(self):
        return self.start==True
    def scearch(self,value):
        temp=self.start
        while temp.next!=None:
            if temp.item==value:
                
                return temp
            else:
            
                return None
    def insert_at_start(self,data):
        n=Node(data,None,self.start)
        self.start=n
    def insert_at_last(self,data):
        n=Node(data)
        temp=self.start
        
        while temp.next!=None:
            temp=temp.next
        temp.next=n
        n.prev=temp
    
        
        
    def insert_after(self,pos,data):
        n=Node(data)
        po=self.scearch(pos)
        temp=self.start
        while temp!=po:
            temp=temp.next
        n.next=temp.next
        n.prev=temp.prev
        po.next=n
        temp.next.prev=po
    def delete_first(self):
        if not self.is_empty():
            self.start=self.start.next
            self.start.next.prev=None
    def delete_last(self):
        temp=self.start
        temp2=self.start.next
        while temp2!=None:
            temp=temp.next
            temp2=temp2.next
        temp.next=None
            
    def delete_pos(self, data):
        po = self.scearch(data)
        if po is None:
            print("Position not found")
            return
        if po.prev is not None:
            po.prev.next = po.next
        if po.next is not None:
            po.next.prev = po.prev
        if po == self.start:
            self.start = po.next

        
    def show(self):
        temp=self.start
        while temp!= None:
            print(temp.item)
            temp=temp.next

mylist=dll()
mylist.insert_at_start(12)
mylist.insert_at_last(34)
mylist.insert_at_last(4)
mylist.insert_at_last(3)
mylist.insert_at_last(6)
mylist.insert_at_last(89)
mylist.insert_after(12,9)
mylist.show()
print("sarfrawrf")
# print(mylist.scearch(12))
# mylist.delete_first()
mylist.delete_last()
# print("after delete")
# mylist.delete_pos(4)
mylist.show()