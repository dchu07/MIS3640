import math
class Point:
    """
    Represents a point in 2_D space

    attributes: x, y
    """
    def __init__(self, x = 0, y = 0):
        self.x = x
        self.y = y

    def __str__(self):
        return f'({self.x}, {self.y}).'

    def __add__(self, other):
        d_x = other.x + self.x
        d_y = other.y + self.y
        return f'({d_x}, {d_y}).'

    def __sub__(self, other):
        d_x = other.x - self.x
        d_y = other.y - self.y
        return f'({d_x}, {d_y}).'
    
    def __eq__(self, other):
        return self.x == other.x
    
    def __contains__(self, number):
        return number == self.x or number == self.y

victoria = Point(3, 4)
print(victoria)

myat = Point(5, 5)
print(victoria + myat)
print(myat - victoria)

carmen = Point(3, 6)
print (carmen == victoria) #true
print (carmen == myat) #false

print(3 in victoria) #true
print(5 in victoria) #false