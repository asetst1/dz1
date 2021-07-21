class Triangle:
    name = "Triangle"
    area = "Площадь треугольника"
    perimeter = "Периметр треугольника"

    def __init__(self, A, B, C):
        self.A = A
        self.B = B
        self.C = C

    def perimeter(self):
        perimeterTriangle = self.A + self.B + self.C
        return perimeterTriangle

    def area(self):
        poluperimeter = 0.5 * (self.A + self.B + self.C)
        areaTriangle = (poluperimeter * (poluperimeter - self.A) * (poluperimeter - self.B) * (
                    poluperimeter - self.C)) ** 0.5
        return areaTriangle


triangle1 = Triangle(A=13, B=14, C=15)

print(triangle1.area())
print(triangle1.perimeter())