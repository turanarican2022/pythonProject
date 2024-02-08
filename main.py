#############################
# @classmethod      #
#############################

class Person:
    
    def __init__(self,name,age):
        self.name = name
        self.age = age
        
    @property
    def give_info(self): # here no argument can be given other than self
        return f"{self.name} is {self.age} years old"
    
    def return_info(self):
        return f"{self.name} is {self.age} years old"
        
