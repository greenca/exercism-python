class Triangle:

    def __init__(self, side1, side2, side3):
        if min(side1, side2, side3) <= 0:
            raise TriangleError('All sides must be greater than zero')
        if max(side1, side2, side3) >= side1 + side2 + side3 - max(side1, side2, side3):
            raise TriangleError('Triangle Inequality violated')
        self.side1 = side1
        self.side2 = side2
        self.side3 = side3

    def kind(self):
        if self.side1 == self.side2 == self.side3:
            return 'equilateral'
        elif self.side1 == self.side2 or self.side1 == self.side3 or self.side2 == self.side3:
            return 'isosceles'
        else:
            return 'scalene'


class TriangleError(ValueError):
    pass
