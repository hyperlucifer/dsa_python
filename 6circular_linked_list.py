'''
circular linked list is a liner data structure 
it is similer like singly linked list but the last node points to the first node
(insted of None) forming a circle
it need to traves all the nodes even if we want to insert/delete the node at start 
insted of taking instance of frist node if we store the last node then it will be 
easier to do oprations 
'''
class Node:
    def __init__(self,item=None,next=None):
        self.item=item
        self.next=next

class cll:
    # here we are keeping treak of last node insted of first node
    # to make operations easy
    def __init__(self,last=None):
        self.last=last
    def is_empty(self):
        return self.last==None
    def insert_at_start(self,data):
        n=Node(data)
        if self.is_empty():
            n.next=n
            self.last=n
        else:
            n.next=self.last.next
            self.last.next=n
        
    def insert_at_last(self,data):
        n=Node(data)
        if self.is_empty():
            n.next=n
            self.last=n
        else:
            n.next=self.last.next
            self.last.next=n
            self.last=n

    def scearch(self,data):
        if self.is_empty():
            return None
        else:
            temp = self.last.next
            while True:
                if temp.item == data:
                    return temp
                temp = temp.next
                if temp == self.last.next:
                    break
            return None
        
    def insert_after(self,pos,data):
        t=self.scearch(pos)
        if t!=None:
            n=Node(data,t.next)
            t.next=n
            if t==self.last:
                self.last=n

    def delete_first(self):
        if not self.is_empty():
            # if list has only one node 
            if self.last.next==self.last:
                self.last=None
            else: 
                self.last.next=self.last.next.next
    
    def delete_last(self):
        if not self.is_empty():
            # if list has only one node 
            if self.last.next==self.last:
                self.last=None
            else: 
                temp=self.last.next
                while temp.next!=self.last:
                    temp=temp.next
                temp.next=self.last.next
                self.last=temp

    def delete_item(self,data):
        if not self.is_empty():
            # if list has only one node 
            if self.last.next==self.last:
                if self.last.item==data:
                    self.last==None
            else: 
                if self.last.next.item==data:
                    self.delete_first()

                else:
                    temp=self.last.next
                    while True:
                        if temp.next.item == data:
                            if temp.next == self.last:
                                self.delete_last()
                            else:
                                temp.next = temp.next.next
                            break
                        temp = temp.next
                        if temp == self.last:
                            break
                    

    def show(self):
        temp=self.last.next
        while True:
            print(temp.item)
            temp=temp.next

            if temp==self.last:
                break


li=cll()
li.insert_at_start(54)
li.insert_at_start(5)
li.insert_at_start(4)
li.insert_at_last(56)
li.scearch(5)
li.insert_after(5,34)
li.show()
print("after deleting")
# li.delete_first()
# li.delete_last()
li.delete_item(54)
li.show()