#############################
# @classmethod              #
#############################

class CarFactory:
    
    manufacturers = []
    
    num_of_cars_produced = 0
    
    cars_produced = []
    
    num_of_cars_in_inventory = 0
    
    def __init__(self, brand, model, year):
        if brand not in CarFactory.manufacturers:
            raise Exception(f"{brand} has no permission to manufacture in this car factory")
        self.brand = brand
        self.model = model
        self.year = year
        CarFactory.record_car(brand,model,year)
    
    def __str__(self):
        return f"here is a {self.brand} {self.model} of year {self.year}"
    
    @classmethod
    def record_car(cls,brand,model,year):
        cls.num_of_cars_produced +=1
        cls.cars_produced.append({"id":cls.num_of_cars_produced,"brand":brand,"model":model,"year":year})
        
    @classmethod
    def sell_car(cls):
        cls.cars_produced.pop()
        cls.num_of_cars_in_inventory -= 1
    
    @classmethod
    def add_manufacturer(cls,manufacturer):
        cls.manufacturers.append(manufacturer)
    
for manufacturer in ["Citroen","Alfa Romeo","Mazda","Fiat"]:
    CarFactory.add_manufacturer(manufacturer)
        
citroen_car = CarFactory("Citroen","C3",2012)

print(citroen_car) # here is a Citroen C3 of year 2012

print(CarFactory.manufacturers) # ['Citroen', 'Alfa Romeo', 'Mazda', 'Fiat']

print(CarFactory.num_of_cars_produced) # 1

print(CarFactory.cars_produced) # [{'id': 1, 'brand': 'Citroen', 'model': 'C3', 'year': 2012}]

alfa_romeo_car = CarFactory("Alfa Romeo","156",2008)

print(alfa_romeo_car) # here is a Alfa Romeo 156 of year 2008

print(CarFactory.manufacturers)  # ['Citroen', 'Alfa Romeo', 'Mazda', 'Fiat']

print(CarFactory.num_of_cars_produced) # 2

print(CarFactory.cars_produced)
# [{'id': 1, 'brand': 'Citroen', 'model': 'C3', 'year': 2012}, 
# {'id': 2, 'brand': 'Alfa Romeo', 'model': '156', 'year': 2008}]

def produce_car(brand,model,year):
    try:
        return CarFactory(brand,model,year)
    except Exception as e:
        return e

print(produce_car("BMW","M4",2024)) # BMW has no permission to manufacture in this car factory
