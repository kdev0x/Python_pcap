class Group:
    def __init__(self):
        self.names = []

    def add_person(self, name):
        self.names.append(name) 

    def print_group(self):
        for p in self.names:
            print(p)

g = Group()
g.add_person("Khalid")
g.add_person("wadee")
g.add_person("abdullah")
g.add_person("sari")

g.print_group()
print("-----------------------")
s = Group()
s.add_person("mohammed")
s.add_person("sultan")
s.add_person("faisal")

s.print_group()
