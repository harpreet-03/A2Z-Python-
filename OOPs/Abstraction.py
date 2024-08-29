'''
Abstraction: 
-------------
 - Abstraction is the concept of hiding the implementation details and showing only the functionality to the user.
 
 - Abstraction can be achieved by using abstract classes and interfaces in Python.

'''
class Car:
    def __init__(self):
        self.acc = False
        self.brk = False
        self.clutch = False
        
    def start(self):
        self.clutch = True
        self.acc = True
        print("car started...")
        
car1  = Car()
car1.start()    