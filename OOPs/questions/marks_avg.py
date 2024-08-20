'''
Ques: 

Create student class that takes name & marks of 3 subjects as arguments in constructor.
Then create a method to print the average.

'''

class Student:
    def __init__(self, name, m1, m2, m3):
        self.name = name
        self.m1 = m1
        self.m2 = m2
        self.m3 = m3
        
    def averageM(self):
        return round((self.m1 + self.m2 + self.m3) / 3, 2)  # Round to 2 decimal places
    
s1 = Student("Naman", 88,77,71)
print("Avergae marks of Naman is", s1.averageM()) 
