'''
A binary tree is defined as a finite set of elements ,called nodes,such that

= T is empty(called the null or empty tree )

= T contains a distingusished node R,called the root of T and the remaining nodes of T
  from an ordered pair of disjoint binary tree T1 and T2

Any node in the binary tree has rither 0,1 or 2 child nodes

types of binary tree 

1)complete binary tree
= All levels are completely filled
  to check the number of nodes in every Level the formula is 2^n n=number of level

2)Almost complete binary tree
= All the levels are completely filled , except possibily the last level and nodes
  in the last level are all left aligned

3)Strict binary tree 
= Each node of a strict binary tree will have either 0 or 2 children


Representation of binary tree

1)Array representation 
2)linked representation
'''
'''
binary search tree 
is the important data structure ,that enables one for search and 
find an element with aberage run time of O(log/2 N)

smaller then value then root on left side ,,,,,,,greater value on right

traversing

preorder-> root left right
inorder -> left root right(it gives the result in sorted order)
postorder->left right root 

deletion 
1)node with no child 
2)node with single child
3)node with 2 childern h
'''
class Node:
    def __init__(self,item=None,left=None,right=None):
        self.item=item
        self.left=left
        self.right=right

class BST:
    def __init__(self) -> None:
        self.root=None
    def insert(self,data):
        self.root=self.rinsert(self.root,data)
    def rinsert(self,root,data):
        if root is None:
            return Node(data)
        if data<root.item:
            root.left=self.rinsert(root.left,data)
        elif data>root.item:
            root.right=self.rinsert(root.right,data)
        
        return root
    def search (self,data):
        return self.rsearch(self.root,data)
    
    def rsearch(self,root,data):
        if root is None or root.item==data:
            return root
        if data<root.item:
            return self.rinsert(root.left,data)
        else:
            return self.rinsert(root.right,data)
        
    def inorder(self):
        result=[]
        self.rinorder(self.root,result)
        return result
    def rinorder(self,root,result):
        if root:
            self.rinorder(root.left,result)
            result.append(root.item)
            self.rinorder(root.right,result)


    def preorder(self):
        result=[]
        self.rpreorder(self.root,result)
        return result
    def rpreorder(self,root,result):
        if root:
            result.append(root.item)
            self.rpreorder(root.left,result)
            self.rpreorder(root.right,result)


    def postorder(self):
        result=[]
        self.rpostorder(self.root,result)
        return result
    def rpostorder(self,root,result):
        if root:
            self.rpostorder(root.left,result)
            self.rpostorder(root.right,result)
            result.append(root.item)
    
    #deletion
    def min_value(self,temp):
        current=temp
        while current.left is not None:
            current=current.left
        return current.item
    def max_value(self,temp):
        current=temp
        while current.right is not None:
            current=current.right
        return current.item
    
    def delete(self,data):
        self.root=self.rdelete(self.root,data)
    def rdelete(self,root,data):
        if root is None:
            return root
        if data <root.item:
            root.left=self.rdelete(root.left,data)
        elif data >root.item:
            root.right=self.rdelete(root.right,data)
        else:
            if root.left is None:
                return root.right
            elif root.right is None:
                return root.left
            root.item=self.min_value(root.right)
            self.rdelete(root.right,root.item)
        return root

b=BST()
b.insert(12)
b.insert(1)
b.insert(2)
b.insert(5)
b.insert(7)
print(b.preorder())
print(b.inorder())
print(b.postorder())
