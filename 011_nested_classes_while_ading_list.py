class Person:
    def __init__(self, first_name, last_name, age) :
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

class Group:
    def __init__(self):
        self.names = []

    def add_person(self, name):
        self.names.append(name) 

    def print_group(self):
        for p in self.names:
            print(p.first_name , p.last_name , p.age)
            print("--------------------------------")

g = Group()
g.add_person(Person("Khalid", "Alqhatani", 13))
g.add_person(Person("wadee", "Altwlayle", 12))
g.add_person(Person("Sary", "alqhatani", 4))

g.print_group()

print(g.names[1].first_name)
