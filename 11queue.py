class queue:
    def __init__(self) -> None:
        self.qu=[]
    
    def enqueue(self,data):
        self.qu.append(data)
    
    def dequeue(self):
        if not self.is_empty():
            self.pop(0)
        else:
            print("the queue is empty")
    def peek(self):
        if not self.is_empty():
            return self.qu[0]
        else:
            print("the queue is empty")
        
    
    def is_empty(self):
        return len(self.qu)==0
    
q=queue()
q.enqueue(21)
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)
q.peek()