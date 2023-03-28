class Student:
    def __init__(self, sid, name, age):
        self.sid = sid
        self.name = name
        self.age = age


students = [
    Student(1, "Khalid", 13),
    Student(2, "Sari", 10),
    Student(3, "Badr", 30)
]

print(students[1].sid)
print(students[2].age)

students[0].age = students[1].age
students[1].name = "Naif"
