class Student:
    def __init__(self, sid, name, age):
        self.sid = sid
        self.name = name
        self.age = age
    
    def print_info(self):
        print(self.sid)
        print(self.name)
        print(self.age)
    

def create_new_student():
    return Student(10, "Khalid", 13)

khalid = create_new_student() #.name
print(khalid)

