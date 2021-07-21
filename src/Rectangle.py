class Rectangle:
    name = "Rectangle"
    area = "Площадь прямоугольника"
    perimeter = "Периметр прямоугольника"

    def __init__(self, storonaA, storonaB):
        self.storonaA = storonaA
        self.storonaB = storonaB

    def area(self):
        areaRectangle = self.storonaA * self.storonaB
        return areaRectangle

    def perimeter(self):
        perimeterRectangle = 2 * (self.storonaA + self.storonaB)
        return perimeterRectangle


rectangle1 = Rectangle(storonaA=10, storonaB=10)

print(rectangle1.area())
print(rectangle1.perimeter())