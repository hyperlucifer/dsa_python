'''
Deque or Double Ended Queue is a generalized version 
of Queue data structure that allows insert and delete at both ends.
'''
class Deque:
    def __init__(self):
        self.de=[]
    
    def insert_front(self,data):
        self.de.insert(0,data)
    
    def insert_rear(self,data):
        self.de.append(data)
    def is_empty(self):
        return len(self.de)==0
    def delete_front(self):
        if not self.is_empty():
            self.de.pop(0)
    def delete_rear(self):
        if not self.is_empty():
            self.de.pop()
    def showFront(self):
        return self.de[0]
    def showRear(self):
        return self.de[len(self.de)-1]
    def size(self):
        return len(self.de)-1
    
