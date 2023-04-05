class Person:
    pass

class Student(Person):
    pass

class MathStudent(Student):
    pass



o1 = Person()
o2 = Student()
o3 = MathStudent()

print(isinstance(o3, Student))
print(isinstance(o3, Person))
print(isinstance(o3, MathStudent))

print(isinstance(o2, Person))
print(isinstance(o1, MathStudent))

print(isinstance(3, int))

print(isinstance(o1,(Person, Student))) # tuple
print(isinstance(o2,(Person, Student))) # tuple
print(isinstance(o3,(Person, Student))) # tuple
