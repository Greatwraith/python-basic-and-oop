# circle_circumference 
# valueOfCircleCircum = 2 * pai * radius

# circle_area
#area = pai * radius ** 2

class Circle:
    pai = 3.14
    def __init__(self, radius):
        self.radius = radius
        
    @classmethod
    def take_thenumber(clr,string):
        import re
        whichCircle = re.findall(r'is \w*', string)
        radiusValue = whichCircle[0][3:]
        return clr(int(radiusValue))
        
    def circumference(self):
        valueOfCircleCircum = 2*Circle.pai*self.radius
        return valueOfCircleCircum
    def area(self):
        area = Circle.pai*self.radius**2
        return area
        
circle1 = Circle.take_thenumber('a circle whose radius is 24')
circle2 = Circle.take_thenumber('a circle whose radius is 23')

# print(circle1.circle_circumference())

circle_objek = [circle1, circle2]

semuanya = {
    'data_lingkaran': []
}

for lingkaran in circle_objek:
    semuanya['data_lingkaran'].append({
        'radius':lingkaran.radius,
        'keliling':lingkaran.circumference(),
        'luas':lingkaran.area()
        
    })

print(semuanya)