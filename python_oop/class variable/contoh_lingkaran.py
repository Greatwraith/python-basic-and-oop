# circle_circumference 
# valueOfCircleCircum = 2 * pai * radius

# circle_area
#area = pai * radius ** 2

class Circle:
    pai = 3.14
    def __init__(self, radius):
        self.radius = radius
        
    def circumference(self):
        valueOfCircleCircum = 2*Circle.pai*self.radius
        return valueOfCircleCircum
    def area(self):
        area = Circle.pai*self.radius**2
        return area
        
circle1 = Circle(24)
circle2 = Circle(23)

print(circle1.circumference())
print(circle1.area())
