'''
__init__ function: (constructor)
------------------
All classes have a function called __init__, which is always executed when an object is being instantiated.

'''
#Creating class:

class Student:
    #default constructor
    def __init__(self):
        print("This is default constructor")
        
    # parameterizes constructor
    def __init__(self, name, age):
        self.name = name
        self.age = age
               
#creating object
s1 = Student("Harpreet", 19)
print(s1.name, s1.age)



'''
The self parameter is a reference to the current instance of the class, 
and is used to access variables that belongs to the class.


'''