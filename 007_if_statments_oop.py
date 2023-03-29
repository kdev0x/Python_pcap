# Python OOP Concept: Methods(actions)
# object: 1- attributes
#         2- actions



class Student:
    def __init__(self, sid, name, age):
        self.sid = sid
        self.name = name
        self.age = age
    
    def print_my_info(self):
        print(self.sid)
        print(self.name)
        print(self.age)
    
    def cmp_age(self, st):
        if self.age > st.age:
            print("self > st")
        elif self.age < st.age:
            print("self < st")
        else:
            print("self = age")


# naif = Student(10, "Naif", 20)
# badr = Student(20, "Badr", 30)

# naif.print_my_info() 
# badr.print_my_info()

# # naif.cmp_age(badr)
# # badr.cmp_age(naif)

# naif.cmp_age(Student(30,"Khalid", 20))

