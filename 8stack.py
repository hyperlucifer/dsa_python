'''
stack is a liner data structure ,,working principle of stack is (LIFO) last in first out
operations
1)push()
2)pop()
3)peek()
4)size()
5)is_empty()
'''
class stack:
    def __init__(self) :
        self.st=[]
    
    def push(self,data):
        self.st.append(data)

    def pop(self):
        if  not self.is_empty():
            return self.st.pop()
        else:
            raise IndentationError("stack is empty")

    def peek(self):
        if not self.is_empty():
            return self.st[-1]
        else:
            raise IndentationError("stack is empty")


    def size(self):
        return len(self.st)

    def is_empty(self):
        return len(self.st)==0

s=stack()
s.push(2)
s.push(9)
s.push(7)
s.push(5)
s.push(4)
print(s.size())
print(s.is_empty())
print(s.peek())
s.pop()
print(s.peek())