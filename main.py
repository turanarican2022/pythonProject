#####################################
# INTRO TO OOP                      #
#####################################

class Person:
    def __init__(self, name, cars):
        self.name = name
        self.cars = cars
    
    def return_info(self):
        return f"{self.name} had these cars: {', '.join(self.cars)}"

halide = Person("Halide",["BMW","Audi"])
print(halide.return_info()) # Halide had these cars: BMW, Audi
print(halide) # <__main__.Person object at 0x7f9d6b457d00>
print(halide.__class__) # <class '__main__.Person'>
print(type(halide)) # <class '__main__.Person'>