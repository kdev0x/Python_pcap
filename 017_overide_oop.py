class Grade:
    def __init__(self, person, the_class, grade):
        self.person = person
        self.the_class = the_class
        self.grade = grade
   
    def print_info(self):
        print("the person is ", self.person, ",", self.person, " is in grade", self.the_class, " ,", self.person ,"'s grade is", self.grade)

class MyGrade(Grade):
    def print_info(self):
        print("the person is -> ", self.person, ",", self.person, " is in grade -> ", self.the_class, " ,", self.person ,"'s grade is ->", self.grade)
       
class FailedGrade(Grade):
    def print_info(self):
        print("the person is ", self.person, ",", self.person, " is in grade", self.the_class, " ,", self.person ,"failed because their grade is", self.grade)

o1 = Grade("Jojo", "class 9", 100)
o2 = MyGrade("Sari", "class 5", 100)
o3 = FailedGrade("Khalid", "class 0.01", 0)
o1.print_info()
o2.print_info()
o3.print_info()
