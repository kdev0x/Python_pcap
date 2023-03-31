 class Pen:
    def __init__(self, name, color, size):
        self.name = name
        self.color = color
        self.size = size

    def write(self, content):
        print("-->", content)
    


class Highliter(Pen):
    def my_highliter(self):
        pass

    def write(self, content):
        print("[[", content)
    
class Pencil (Highliter):
    def my_pencil(self):
        pass 

    def write(self, content):
        print("**", content)


p1 = Pen("Any", "red", 1)
p2 = Highliter("New", "blue", 2)
p3 = Pencil("xyz", "black", 1)

p1.write("Welcome to Python")
p2.write("Welcome to Python")
p3.write("Welcome to Python")

