#######################################
# @staticmethod                       #
########################### to Ethan...

class Student:
    def __init__(self,name,age):
        self.name=name
        self.age = age
    
    def __str__(self):
        return f"{self.name} is {self.age} years old."
    
    @staticmethod
    def school_age(age):
        return f"a kid must be at least {age} years old to begin school"
    
print(Student.school_age(7))
# a kid must be at least 7 years old to begin school