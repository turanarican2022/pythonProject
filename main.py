#######################################
# raising error and isinstance()      #
########################### to Ethan...

class Student:
    
    _students = []
    
    def __init__(self,name,age):
        if age < 7:
            raise ValueError("This kid is too young to be a student.")
        self.name = name
        self.age = age
        Student._add_student(name,age)
    
    @classmethod
    def _add_student(cls,name,age):
        cls._students.append({"name":name,"age":age})
        
    @classmethod
    def students_info(cls):
        return [f'{student["name"]} is {student["age"]} years old' for student in cls._students]
    
    def __str__(self):
        return f"{self.name} is {self.age} years old."

    
ethan = Student("Ethan",19)
print(isinstance(ethan,Student)) # True
halit = Student("Halit",14)
print(Student.students_info()) # ['Ethan is 19 years old', 'Halit is 14 years old']
turan = Student("Turan",6) # ValueError: This kid is too young to be a student.

