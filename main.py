#######################################
# @staticmethod                       #
########################### to Ethan...

class Student:
    def __init__(self,name,age,school):
        self.name = name
        self.age = age
        self.school = school
        
    def __str__(self):
        return f"{self.name} is {self.age} years old and a succesful student at {self.school}"
    
    @classmethod
    def from_dashed_string(cls,dashed_str):
        name,age,school = dashed_str.split("-")
        cls(name,age,school)
        
print(Student("Ethan",19,"MIT"))
# Ethan is 19 years old and a succesful student at MIT