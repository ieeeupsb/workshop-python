from math import pi

class Shape:
    def __init__(self):
        pass

    def area(self):
        return 0


class Cicrle(Shape):
    def __init__(self, radius):
        Shape.__init__(self)
        self.radius = radius

    def area(self):
        return (pi*self.radius)**2


class Rectangle(Shape):
    def __init__(self, l1, l2):
        Shape.__init__(self)
        self.l1 = l1
        self.l2 = l2

    def area(self):
        return self.l1*self.l2

class Square(Rectangle):
    def __init__(self, length):
        Rectangle.__init__(self, length, length)

    #don't need to override the area method from rectangle because it already does what we need
