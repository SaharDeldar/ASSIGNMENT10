class Shape:

    def __init__(self):
        self.mohit = 0
        self.masahat = 0
        
class Circle(Shape):

    def __init__(self, radius):
        Shape.mohit = (radius * 2) * 3.14
        Shape.masahat = (radius * radius) * 3.14

    def show_mohit(self):
        return Shape.mohit

    def show_masahat(self):
        return Shape.masahat


class Rectangle(Shape):

    def __init__(self, length, breadth):
        Shape.mohit = (length + breadth) * 2
        Shape.masahat = length * breadth

    def show_mohit(self):
        return Shape.mohit

    def show_masahat(self):
        return Shape.masahat




r = Rectangle(4, 5)
print(f"Rectangle perimeter: {r.show_mohit()} area: {r.show_masahat()}")
c = Circle(3 / 3.14)
print(f"Circle perimeter: {c.show_mohit()} area: {c.show_masahat()}")