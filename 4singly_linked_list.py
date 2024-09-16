'''
1)What is list in genral?
= list is a linear collection of data items also known as list items  

as the python is dymamicly typed there for the linked list in python can store 
data of datatype in a list (but in java,c/cpp the data type of the elements 
must be same althrow the list) 
python assign the type by its value ,,not by making variable

What is node?
node is a object of a user define class node which consist of two things data 
,and a referance variable to a next object 

the first object will have refernce to the second object,,and the referance of the first 
object is stored in a new seperate variable called start or head

the start object is of class singly linked list ,,and after that all classes are of node class

the last node will have referance of none

what is singly linked list?
SLL is a liner data structure
it has only one reference variable and grow only in one direction
it can grow and srink

operation's on SLL(make all this operations is SLL class)
a)insetion(at start,at last,insert position,after a perticular node)
b)delete(first,last,at position)
c)is empty
d)traverse





del keyword delete a referance variable not a object
'''
class Node:
    def __init__(self,item=None,next=None):
        self.item=item
        self.next=next

class SLL:
    def __init__(self,start=None) -> None:
        self.start=start
    def isEmpty(self):
        return self.start==None
    def insert_at_start(self,data):
        n=Node(data,self.start)
        self.start=n
    def insert_at_last(self,data):
        n=Node(data)
        if not self.isEmpty():
            temp=self.start
            while temp.next != None:
                temp=temp.next
            temp.next=n
        else:
            self.start=n
    def search(self,data):
        temp=self.start
        while temp.next != None:
            if temp.item==data:
                return temp
            temp=temp.next
        return None
    def insert_after(self,value,data):
        temp =self.search(value)
        if temp!=None:
            n=Node(data,temp.next)
            temp.next=n
        else:
            return None
    
    def print_list(self):
        temp=self.start
        while temp!=None:
            print(temp.item )
            temp=temp.next
    # deleting------------
    def delete_First(self):
        self.start=self.start.next
    def delete_last(self):
        temp=self.start
        while temp.next.next!=None:
            temp=temp.next
        temp.next=None
        
    def delete_perticuar(self,data):
        temp=self.start
        if temp.item==data:
            self.delete_First()
        else:
            while temp.next is not None:
                if temp.next.item==data:
                    temp.next=temp.next.next
                    break
    def __iter__(self):
        return sll_iterator(self.start)
    
class sll_iterator:
    def __init__(self,start) -> None:
        self.curr=start
    def __iter__(self):
        return self
    def __next__(self):
        if not self.curr:
            raise StopIteration
        data=self.curr
        self.curr=self.curr.next
        return data.item

myList=SLL()
myList.insert_at_start(12)
myList.insert_at_last(1)
myList.insert_after(12,7)
myList.insert_at_start("we")
myList.print_list()
print("after deleting")
# myList.delete_First()
# myList.delete_last()
myList.delete_perticuar(7)
myList.print_list()
for item in myList:  # myList is the SLL object
    print(item)