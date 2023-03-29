class Student:
    def __init__(self, sid, name, age):
        self.sid = sid
        self.name = name
        self.age = age
    
    def print_info(self):
        print(self.sid)
        print(self.name)
        print(self.age)

students = [
    Student(10,"Khalid",13),
    Student(20,"Wade",15),
    Student(30,"Aljawarah",12),
    Student(40,"Sari",9)
]

for student in students:
    student.print_info()
    print("--------------------")
    
