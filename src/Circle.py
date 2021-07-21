from math import pi


class Circle:
    name = "Circle"
    area = "Площадь круга"
    perimeter = "Периметр круга"

    def __init__(self, radius):
        self.radius = radius

    def area(self):
        areaCircle = pi * self.radius ** 2
        return areaCircle

    def perimeter(self):
        perimeterCircle = 2 * pi * self.radius
        return perimeterCircle


circle1 = Circle(radius=10)

print(circle1.area())
print(circle1.perimeter())