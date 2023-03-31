class Person:
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname

  def printname(self):
    print(self.firstname, self.lastname)


class Student(Person):
    def my_function(self):
        print("student")


class MathStudent(Student):
    def my_math_code(self):
        print("math function")


p = Person("Khalid", "Alqahtani")
s = Student("Sari", "Alqahtani")
m = MathStudent("Aljawharah", "Alqahtani")


p.printname()
s.printname()
m.printname()

# p.my_function()
s.my_function()
m.my_function()

p.my_math_code() # error error
s.my_math_code() # true true
m.my_math_code() # true true

p.firstname = "Khalid"
s.firstname = "Sari"
m.firstname = "Aljawharh"
