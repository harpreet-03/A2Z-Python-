'''
class.attr
obj.attr

Note : obj attr > class attr

'''
'''

Explanation :
--------------

- Class Attributes: These are attributes that are shared among all instances (objects) of a class. They are defined within the class but outside any methods.

- Instance Attributes: These are attributes that are unique to each instance of a class. They are typically defined inside the constructor method (__init__).

'''

class Car:
    wheels = 4  # Class attribute
    
    def __init__(self, color):
        self.color = color  # Instance attribute

# Creating instances (objects) of the class Car
car1 = Car("red")
car2 = Car("blue")

# Accessing instance attributes using obj.attr
print(car1.color)  # Output: red
print(car2.color)  # Output: blue

# Accessing class attribute using obj.attr
print(car1.wheels)  # Output: 4
print(car2.wheels)  # Output: 4
