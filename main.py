#############################
# @ PROPERTY DECORATOR      #
#############################

# if a method's (function inside a class) sole job is
# returning a value @property decorator can be used 
# and now we don't need parantheses to get that value 
# when calling that method

class Person:
    
    def __init__(self,name,age):
        self.name = name
        self.age = age
        
    @property
    def give_info(self): # here no argument can be given other than self
        return f"{self.name} is {self.age} years old"
    
    def return_info(self):
        return f"{self.name} is {self.age} years old"
        

person=Person("Nitissa",42)
print(person.give_info) # Nitissa is 42 years old
print(person.return_info)
# <bound method Person.return_info of <__main__.Person object at 0x7f247d617d00>>