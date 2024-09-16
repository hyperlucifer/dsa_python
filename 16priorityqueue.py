'''
A priority queue is a collection of elements such that each element has been asign a priority

rules 
1)any element of higher priority is processed befour any element of lower priority
2)two element with the same priority are procedssed according to the order in which they were added in 
  priority queue

  operations 
  pop()
  push()
  isempty()
  size()

  using list  
'''
class priorityQueue:
    def __init__(self) -> None:
        self.items=[]
    def push(self,data,priority):
        index=0
        while index<len(self.items) and self.items[index][1]<=priority:
            index+=1
        self.items.insert(index,(data,priority))
    def is_empty(self):
        return len(self.items)==0
    def pop(self):
        if self.is_empty():
            raise IndexError("queue is empty")
        return self.items.pop(0)[0]

    def size(self):
        return len(self.items)
    
p=priorityQueue()
p.push("sheth",4)
p.push("mothi",2)
p.push("mansa",7)
p.push("ayyeee",1)
p.push("mo",2)

while not p.is_empty():
    print(p.pop())