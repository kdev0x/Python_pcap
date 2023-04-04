class Student:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    def print_info(self):
        print("Student: ", self.first_name, self.last_name)
    

class MathStudent(Student):
    def __init__(self, first_name, last_name, age):
        Student.__init__(self, first_name, last_name)
        self.age = age
    
    def print_info(self):
        print("MathStudent: ", self.first_name, self.last_name, self.age)


class AdvancedMathStudent(MathStudent):
    def __init__(self, first_name, last_name, age, address):
        MathStudent.__init__(self, first_name, last_name, age)
        self.address = address
    

    def print_info(self):
        print("AdvancedMathStudent: ", )


std = Student("Naif", "Saleh")
mstd = MathStudent("Badr", "Abdullah", 20)
astd = AdvancedMathStudent("Sari", "Alqahtani", 10, "KSA")

print(std.first_name)
print(mstd.first_name)
print(astd.first_name)
