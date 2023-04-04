class Shape:
    def __init__(self, shape_name):
        self.shape_name = shape_name

    def draw(self):
        print(self.shape_name)


class Rectangle(Shape):
    def __init__(self, height, width):
        super().__init__("Rectangle")
        self.height = height
        self.width = width
       
    def draw(self):
        print(self.shape_name, self.height, "X", self.width)

class Triangle(Shape):
    def __init__(self, side):
        super().__init__("Triangle")
        self.side = side

    def draw(self):
        print(self.shape_name, self.side )

class Circle(Shape):
    def __init__(self , radius):
        super().__init__("Circle")
        self.radius = radius

    def draw(self):
        print(self.shape_name , self.radius)


r = Rectangle(50, 100)
r.draw()

t = Triangle(27)
t.draw()

c = Circle(360)
c.draw()
