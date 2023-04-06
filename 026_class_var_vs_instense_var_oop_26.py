class Student:
    #class variable
    school_name = "My School"
    school_address = "KSA"
    num_of_student = 0

    def __init__(self, name, age):
        self.name = name #instance variable
        self.age = age
        Student.num_of_student = Student.num_of_student + 1


s1 = Student("Sari", 11) #instance object
s2 = Student("Kahlid", 13)
s3 = Student("Aljawharh", 15)

print(s1.name)
print(s2.name)
print(s3.name)

print(Student.school_name)
print(Student.school_address)

# instance variable vs class variable

print(Student.num_of_student)
