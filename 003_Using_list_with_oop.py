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

for s in students:
    if s.sid == 2:
        continue
    print(s.sid, s.name, s.age)


