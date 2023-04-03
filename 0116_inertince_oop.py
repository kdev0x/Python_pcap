class Student:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
    
    def print_info(self):
        print(self.first_name, self.last_name)


class MathStudent(Student):
    def print_info(self): #override
        print("[", self.first_name, "]-> ", self.last_name)


m1 = Student("Khalid", "Alqahtani")
m2 = MathStudent("Sari", "Alqahtani")

m1.print_info()
m2.print_info()
