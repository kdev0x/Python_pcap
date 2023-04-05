class Person:
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

class MyPerson(Person):
    def __init__(self, first_name, last_name, age, address):
        super().__init__(first_name, last_name, age)
        self.address = address

class Group:
    def __init__(self):
        self.names = []
    def add(self, person):
        self.names.append(person)

    def print_info(self):
        for person in self.names:
            if isinstance(person, MyPerson):
                print("[", person.first_name, "], ", person.last_name, person.age, person.address)
            elif isinstance(person, Person):
                print("[", person.first_name, "], ", person.last_name, person.age)




group = Group()

# o1 = Person("aljawharah", "LQAHTANI", 12939)
# group.add(o1)

group.add(Person("khalid", "alqahtani", 474))
group.add(MyPerson("khalid","alqhatani",13,"hittin 1378"))

group.print_info()


# o1 = Person("aljawharah", "LQAHTANI", 12939)
# o2 = MyPerson("aljawharah", "LQAHTANI", 12939, "abc")


# print(isinstance(o1, Person))
# print(isinstance(o2, Person))
# print(isinstance(o1, MyPerson))
# print(isinstance(o2, MyPerson))
