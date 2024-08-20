class AreaOfSquare:
    def __init__(self, side):
        self.side = side  # Instance attribute
    
    def area(self):
        return self.side * self.side  # Using self.side
    
    def perimeter(self):
        return 4 * self.side  # Using self.side
    
    '''
    self is compulsory in instance methods to refer to the instance itself.
    Omitting self leads to errors or loss of context, making it impossible to access instance attributes.
    '''
    
# Creating an instance
square1 = AreaOfSquare(5)

# Calculating and printing the area and perimeter
print("Area of square:", square1.area())  # Output: Area of square: 25
print("Perimeter of square:", square1.perimeter())  # Output: Perimeter of square: 20
