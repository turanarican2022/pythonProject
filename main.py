#############################
# INHERITANCE               #
#############################

class Person:
    
    nationality = "Israel"
    
    def __init__(self,name,age):
        self.name = name
        self.age = age
    
    def person_info(self):
        return f"{self.name} is {self.age} years old"
    
class Teacher(Person):
    
    def __init__(self,name,age,job,salary):
        super().__init__(name,age)
        self.job = job
        self.salary=salary
    
    def teacher_info(self):
        return f"{self.name} is a {self.job} and their salary is {self.salary}"
    
class Student(Person):
    
    def __init__(self, name, age, job, school):
        super().__init__(name, age)
        self.job = job
        self.school=school
        self.grades = []
        
    def student_info(self):
        return f"{self.name} is a {self.age} year old {self.job} at {self.school}"
    
    def add_grade(self,g):
        self.grades.append(g)
    
    def avg_grades(self):
        return sum(self.grades)/len(self.grades)
    

teacher_assida = Teacher("Assida", 29, "teacher", 28000)
print(teacher_assida.teacher_info())
# Assida is a teacher and their salary is 28000
print(teacher_assida.nationality)
# Israel
teacher_assida.nationality = "Danish"
print(teacher_assida.nationality)
# Danish

student_ethan = Student("Ethan",42,"Student","MIT")
student_ethan.add_grade(50)
student_ethan.add_grade(100)
print(student_ethan.person_info())
# Ethan is 42 years old
print(student_ethan.student_info())
# Ethan is a 42 year old Student at MIT
print(student_ethan.avg_grades())
# 75.0
print(student_ethan.nationality)
# Israel