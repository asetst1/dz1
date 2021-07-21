class Square:
    name = "Square"
    area = "Площадь квадрата"
    perimeter = "Периметр квадрата"

    def __init__(self, sizeA):
        self.sizeA = sizeA

    def area(self):
        areaSquare = self.sizeA * self.sizeA
        return areaSquare

    def perimeter(self):
        perimeterSquare = 4 * self.sizeA
        return perimeterSquare


square1 = Square(sizeA=10)

print(square1.area())
print(square1.perimeter())