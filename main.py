#######################################
# using @classmethod as a constructor #
################### to Ethan & Halit...

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
        
ethan = Student("Ethan",19,"MIT")
print(ethan)
# Ethan is 19 years old and a succesful student at MIT

halit = Student("Halit",14,"Afyon M.P.A. Lisesi")
print(halit)
# Halit is 14 years old and a succesful student at Afyon M.P.A. Lisesi
