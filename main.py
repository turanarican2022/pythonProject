#############################
# @classmethod              #
#############################

class CarFactory:
    
    _manufacturers = []
    
    _num_of_cars_produced = 0
    
    _cars_produced = []
    
    _num_of_cars_in_inventory = 0
    
    def __init__(self, brand, model, year):
        if brand not in CarFactory._manufacturers:
            raise ValueError(f"{brand} has no permission to manufacture in this car factory")
        self.brand = brand
        self.model = model
        self.year = year
        CarFactory._record_car(brand,model,year)
    
    def __str__(self):
        return f"here is a {self.brand} {self.model} of year {self.year}"
    
    @classmethod
    def _record_car(cls,brand,model,year):
        cls._num_of_cars_produced +=1
        cls._cars_produced.append({"id":cls._num_of_cars_produced,"brand":brand,"model":model,"year":year})
        
    @classmethod
    def sell_car(cls):
        cls.cars_produced.pop()
        cls._num_of_cars_in_inventory -= 1
    
    @classmethod
    def add_manufacturer(cls,manufacturer):
        cls._manufacturers.append(manufacturer)
    
for manufacturer in ["Citroen","Alfa Romeo","Mazda","Fiat"]:
    CarFactory.add_manufacturer(manufacturer)
        
citroen_car = CarFactory("Citroen","C3",2012)

print(citroen_car) # here is a Citroen C3 of year 2012

print(CarFactory._manufacturers) # ['Citroen', 'Alfa Romeo', 'Mazda', 'Fiat']

print(CarFactory._cars_produced) # [{'id': 1, 'brand': 'Citroen', 'model': 'C3', 'year': 2012}]

alfa_romeo_car = CarFactory("Alfa Romeo","156",2008)

print(alfa_romeo_car) # here is a Alfa Romeo 156 of year 2008

print(CarFactory._cars_produced)
# [{'id': 1, 'brand': 'Citroen', 'model': 'C3', 'year': 2012}, 
# {'id': 2, 'brand': 'Alfa Romeo', 'model': '156', 'year': 2008}]

def produce_car(brand,model,year):
    try:
        return CarFactory(brand,model,year)
    except ValueError as e:
        return e

print(produce_car("BMW","M4",2024)) # BMW has no permission to manufacture in this car factory
