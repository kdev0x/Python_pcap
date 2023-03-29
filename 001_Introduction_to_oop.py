class Company:
    def __init__(self, name, year):
        self.name = name
        self.year = year
 
class Computer:
    def __init__(self, name, color, ram, comp):
        self.name = name
        self.color = color
        self.ram = ram
        self.company = comp

class Person:
   def __init__(self, f_name , l_name, age, cmp): # Constructor
        self.first_name = f_name
        self.last_name = l_name 
        self.age = age
        self.computer = cmp

aljawharah = Person("aljawharah", "alqahtani", "14", Computer("macbook", "blue", 128, Company("khalid_law", 1876) ))
print(aljawharah.first_name)
print(aljawharah.last_name)
print(aljawharah.age)
print(aljawharah.computer.name)
print(aljawharah.computer.color)
print(aljawharah.computer.ram)
print(aljawharah.computer.company.name)
print(aljawharah.computer.company.year)




#khalid = Person("khalid", "alqhatani", 15, Computer("msi_titan_gt77", "black", 8192))
#print(khalid.computer.name)
#print(khalid.computer.ram)
#khalid = Person("Khalid", "Alqhatani", 15)
#print(khalid.first_name)
 

#msititan = Computer("msititan", "black", 128)
#msi_titan_gt77 = Computer("msi_titan_gt77", "mate_black", 128)
#print(msititan.name, msititan.color, msititan.ram)
#print(msi_titan_gt77.name, msi_titan_gt77.color,msi_titan_gt77.ram)
