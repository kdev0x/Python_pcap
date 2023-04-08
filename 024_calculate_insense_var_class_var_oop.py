# instance varaibles vs class variables
# num of instance and num of instance variables

class Person:
    student = "aljawharah"
    num_of_instance = 0
    num_of_instance_variables = 0 
    num_of_class_variables = 4

    def __init__(self, name, grade, theclass):
        self.name = name
        self.grade = grade
        self.theclass = theclass
        self.values = [1, 2, 3, 4]
        Person.num_of_instance = Person.num_of_instance + 1
        Person.num_of_instance_variables = Person.num_of_instance * 4

   
o1 = Person("Sari",99,6)
o2 = Person("aljawahra",48,3)
o3 = Person("khlid",100,6)

print( Person.num_of_class_variables)

print(Person.student)
print(Person.num_of_instance , Person.num_of_instance_variables)
