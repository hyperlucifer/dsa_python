class Node:
    def __init__(self, item=None, prev=None, next=None):
        self.item = item
        self.prev = prev
        self.next = next

class CDLL:
    def __init__(self, last=None):
        self.last = last

    def is_empty(self):
        return self.last is None

    def search(self, val):
        if self.is_empty():
            return None
        temp = self.last.next
        while True:
            if temp.item == val:
                return temp
            if temp == self.last:
                break
            temp = temp.next
        return None

    def insert_at_start(self, data):
        n = Node(data)
        if self.is_empty():
            n.next = n
            n.prev = n
            self.last = n
        else:
            n.next = self.last.next
            n.prev = self.last
            self.last.next.prev = n
            self.last.next = n

    def insert_at_last(self, data):
        n = Node(data)
        if self.is_empty():
            n.next = n
            n.prev = n
            self.last = n
        else:
            n.next = self.last.next
            n.prev = self.last
            self.last.next.prev = n
            self.last.next = n
            self.last = n

    def insert_after(self, pos, data):
        p = self.search(pos)
        if p is None:
            print("Element not found")
            return
        n = Node(data)
        n.next = p.next
        n.prev = p
        p.next.prev = n
        p.next = n
        if p == self.last:
            self.last = n

    def delete_first(self):
        if self.is_empty():
            return
        if self.last.next == self.last:
            self.last = None
        else:
            self.last.next = self.last.next.next
            self.last.next.prev = self.last

    def delete_last(self):
        if self.is_empty():
            return
        if self.last.next == self.last:
            self.last = None
        else:
            self.last.prev.next = self.last.next
            self.last.next.prev = self.last.prev
            self.last = self.last.prev

    def show(self):
        if not self.is_empty():
            t = self.last.next
            while True:
                print(t.item, end=" ")
                if t == self.last:
                    break
                t = t.next
            print()

# Example usage
cd = CDLL()
cd.insert_at_start(23)
cd.insert_at_start(3)
cd.insert_at_last(45)
cd.insert_at_last(7)
cd.insert_after(45, 90)
cd.show()

print("After delete:")
# cd.delete_first()
cd.delete_last()
cd.show()
