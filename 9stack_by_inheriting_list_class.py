from typing import SupportsIndex


class stack(list):
    def is_empty(self):
        return len(self)==0
    
    def push(self,data):
        self.append(data)
    
    def pop(self):
        if not self.is_empty():
            return super().pop()
        else:
            raise IndexError("stack is empty")
        
    def peek(self):
        if not self.is_empty():
            return self[-1]
        else:
            raise IndexError("stack is empty")
    
    def insert(self, index,data):
        raise AttributeError("no attribute 'insert' in stack")
        
    def size(self):
        return len(self)
    
s1=stack()
s1.push(32)
s1.push(2)
s1.push(5)
s1.push(3)
print(s1.peek())