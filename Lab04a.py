import math

class Shape:
    __number_of_shapes = 0
    def __init__(self, name="Shape"):
        self.__name = name
        Shape.__number_of_shapes += 1
    def find_area(self):
        return 0
    def find_perimeter(self):
        return 0
    def display(self, end=""):
        print (f"This is a {self.__name:s}{end:s}")
    def get_number_of_shapes():
        return Shape.__number_of_shapes

class Circle(Shape):
    def __init__(self, radius, name="Circle"):
        super().__init__(name)
        self.__radius = radius
    def find_area(self):
        return self.__radius * self.__radius * math.pi
    def find_perimeter(self):
        return self.__radius * math.pi * 2
    def display(self, end=""):
        super().display(f" with area = {self.find_area():.2f}, perimeter = {self.find_perimeter():.2f}{end:s}")
            
class Rectangle(Shape):
    def __init__(self, length, width, name="Rectangle"):
        super().__init__(name)
        self.__length = length
        self.__width = width
    def find_area(self):
        return self.__length * self.__width
    def find_perimeter(self):
        return (self.__length + self.__width) * 2
    def display(self, end=""):
        super().display(f" with area = {self.find_area():.2f}, perimeter = {self.find_perimeter():.2f}{end:s}")

class RightAngledTriangle(Shape):
    def __init__(self, base_length, height, name="Right-angled Triangle"):
        super().__init__(name)
        self.__base_length = base_length
        self.__height = height
    def find_area(self):
        return self.__base_length * self.__height / 2
    def find_perimeter(self):
        return (self.__base_length ** 2 + self.__height ** 2) ** 0.5 + self.__base_length + self.__height
    def display(self, end=""):
        super().display(f" with area = {self.find_area():.2f}, perimeter = {self.find_perimeter():.2f}{end:s}")

class Cylinder(Circle):
    def __init__(self, radius, length, name="Cylinder"):
        super().__init__(radius, name)
        self.__length = length
    def find_area(self):
        return super().find_area() * 2 + super().find_perimeter() * self.__length
    def find_perimeter(self):
        return super().find_perimeter() * self.__length
    def find_volume(self):
        return super().find_area() * self.__length
    def display(self, end=""):
        super().display(f", volume = {self.find_volume():.2f}{end:s}")
        
#You are NOT allowed to modify following codes
if __name__=="__main__":
    list_shape = list()
    list_shape.append(Shape())
    list_shape.append(Shape("Pentagon"))
    list_shape.append(Circle(1))
    list_shape.append(Rectangle(2,2))
    list_shape.append(RightAngledTriangle(3,4))
    list_shape.append(Cylinder(1,3))
    for shape in list_shape:
        shape.display()
    print (f"There are {Shape.get_number_of_shapes()}"
           f" shapes in total")
