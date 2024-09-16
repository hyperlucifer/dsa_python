# common noun is a class eg doctor
# the proper noun is a object eg dr munna

# object can contains it's class characters and perform some actions to change or access it

# encapsulation = An act of combining properties and methods related same object is 
#                 known as encapsulation like class
#
# class is a group of variables and funcations ,class is description of an object
# it a user define data type
#
# in python the properties and function are called attributes(but in other lang only 
# properties are called attributes) 
# but in python the name of function is also a referance variable 

# object is a instance of a class , it a way to represent a real world entities

# there are two types of objects in python 
# 1) class object
#   = in python if we write a name of function/classname without brackets then we repreasent a 
#     referance of that function/classname ,,,but when we give brackets it represent a function
#     call then  it will automaticaly call a function/classname that will make a object of that class and 
#     return a referance of it

#     function/classname without brackets then it is a class object,,there can be only one class
#     object of a class  
#     we dont have to make the class object explicitly it made automatically sa soon as we make a class
#     class name is reference variable that is refering the class object
#     eg.test  ,,,, test()
# 2) instance object
# = it is the normal object we make in the code,we can make multiple instance 
#   object of a class 
# ----------------------------------------------------------------------------------------------
# every variable in a class object body is a class variable 
'''
there are many ways to make instance object variable
1) by using init method ,,it is similer as constroctor ,,, when we make an instance object it 
   it will call the init method and pass that object in init as an argument
'''
class test:
    x=34 # static/class variable 
    def __init__(self) -> None:
        self.a=9 #instance var
        self.b=8
    
        #instance method
    def abc(self)->None:
        pass
    # these two method below will work on class object
        #stactic method
    @staticmethod
    def st()->None:
        print("sheth")
        #class method
    @classmethod
    def cm(cls)->None:
        print(cls.x)
t1=test()
t2=test()
print(t1.a)
print(t2.a)
test.cm() #it implistly pass the class as an argument to that function
test.st()
'''
-----------methods-------- 
1)instance method
= if we want to make a method the method of a instance object then the first argument must
  be the self
2)static method
= if we want to make static method then we dont need self argument but we need @staticmethod 
  decorater
  we should call this method using class name or object name too
  it can also access class methods and vatiables
3)class method
=if we want to make class method then we need one argument (cls) and we need a @classmethod 
   decorater
   it works on class object to manipulate class variables and methods
   we should call this method using class name
'''