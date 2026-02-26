# Performing special operations
# triangle area


class Triangle:
    def __init__(self, base, height):
        self.base = base
        self.height = height    
    def calculate_area(self):
        return 0.5 * self.base * self.height
    def __add__(self, other):
        return self.calculate_area() + other.calculate_area()
    
triangle1 = Triangle(10, 5)
triangle2 = Triangle(6, 8)
print("Area of triangle 1: ", triangle1.calculate_area())
print("Area of triangle 2: ", triangle2.calculate_area())

print("The area of both triangles is : ", triangle1 + triangle2)