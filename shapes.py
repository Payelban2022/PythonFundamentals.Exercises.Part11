class Rectangle:
    def __init__(self,l,w):
        self.length = l
        self.width = w

    def area(self):
        return self.length * self.width

    def perimeter(self):
        return 2*(self.length + self.width)


class Square(Rectangle):
    def __init__(self,side):
        super().__init__(side,side)
