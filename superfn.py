class Rectangle():
    def __init__(self, length, width):
        self.length = length
        self.width = width

class Square(Rectangle):
    def __init__(self, length, width):
        super().__init__(length,width) 
    def area(self):
        return self.length*self.width

class Cube(Rectangle):

    def __init__(self, length, width, height):
        super().__init__(length,width) 
        self.height = height
    def vol(self):
        return self.length*self.width*self.height    


square = Square(3,3)
cube = Cube(3,3,3)

print(cube.vol())
print(square.area())
        