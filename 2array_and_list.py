# making array in python
# array is a collection of a simmiler data type 
# all the elements are indexed
# they are in continous memory location
# array is fixed sized (but not in python.)

# in python array is not provided built in like java or c lang

# list = is in the ,module called builtins
# arrays = are in the module called array
# array is not builtin data structure and there fore it need to be impoted  

# in this array module defines an object type which can be efficiently 
# represrent an array of basic values

# syntax =a1=array(type code,[elements])
from array import *
a=array('i',[12,43,65,23,65,3])
print(type(a))
for i in a:
    print(i)
print("wdf")
a.append(43)

i=0
while (i<len(a)):
    print(a[i])
    i+=1

print(a.count(43))
#pop delete the element by index value 
#remove the element by value
#---------------list---------------
'''
list is a class
list is mutable
list elements are indexed 
list is an iterable 
list can grow(dynamic array)
list can contain different type elements
'''
l1=[2,"7",9.9]
print(l1)