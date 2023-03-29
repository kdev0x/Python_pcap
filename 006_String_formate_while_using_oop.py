class Student:
    def __init__(self, sid, name, age):
        self.sid = sid
        self.name = name
        self.age = age

students = [
    Student(10, "Khalid", 1024),
    Student(20, "Aljwhara", 512),
    Student(30, "Tawfiq", 4096)
]

for student in students:
    print("<"+str(student.sid)+">", "["+student.name+"]", "["+str(student.age)+"]")
 
