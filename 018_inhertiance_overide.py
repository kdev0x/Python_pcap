class Homework:
    def __init__(self,name,grade):
        self.name = name
        self.grade = grade
    
    def print_info(self):
        print("Homework: he name of the person is ", self.name , " and the grade is", self.grade)

class VeryEasyHomework(Homework):
    def print_info(self):
        print("VeryEasyHomework: The name is ", self.name , " and the grade is ", self.grade)

class EasyHomework(VeryEasyHomework):
    def print_info(self):
        print("EasyHomework: The name is ",self.name , "and the grade is" , self.grade)
    


home_work_1 = Homework("aljawahra", 21)
home_work_1.print_info()
home_work_2 = VeryEasyHomework("Khalid", 102)
home_work_2.print_info()
home_work_3 = EasyHomework("sari",-120)
home_work_3.print_info()
