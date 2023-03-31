class Group:
    def __init__(self):
        self.names = []
    
    def add_person(self, name):
        self.names.append(name)
    
    def start(self):
        print("--------------------------------------")
        return self
    
    def end(self):
        print("****************************************")
        return self
    
    def print_info(self):
        for name in self.names:
            print(name)
        return self
    
    def my_code(self):
        return "code"


my_group = Group()
my_group.add_person("one")
my_group.add_person("two")
my_group.add_person("three")

my_group.start().print_info().end().my_code()
my_group.start().start().start().print_info().print_info().end().end().my_code()

my_group.start()
my_group.print_info()
my_group.end()
