class queue(list):
    def is_empty(self):
        return len(self)==0
    def enqueue(self,data):
        self.append(data)
    def pop(self):
        super().pop()
    def peek(self):
        return self[0]
    
qw=queue()

    