class Course:
    def __init__(self,instructor,subject,description):
        self.instructor  = instructor
        self.subject = subject
        self.description = description
        self.rating = 0

    def print(self):
        print(self.instructor , self.subject , self.description)
    
    def __str__(self):
        return self.subject + ", " + self.description + ", " + self.instructor

    def set_rating(self,rating):
        self.rating = rating


class Courses:
    def __init__(self):
        self.courses = []

    def add(self, course):
        self.courses.append(course)

    def __len__(self):
        return len(self.courses)

    def __contains__(self, subject):
        for course in self.courses:
            if subject == course.subject:
                return True
        return False

    def print(self):
        for course in self.courses:
            print(course) 

c = Courses()

c.add(Course("sari", "C", "long course"))
c.add(Course("aljawharah","python","good course"))
c.add(Course("khalid","html","very very easy"))

print(len(c))

print("Java" in c)
print("python" in c)

c.print()
