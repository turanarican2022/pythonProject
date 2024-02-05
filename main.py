#############################
# MAGIC __magic__() METHODS #
#############################

class Garage:
    def __init__(self):
        self.cars = []
        
    def __len__(self):
        return len(self.cars)
    
    def __getitem__(self,i):
        return self.cars[i]
    
    def __repr__(self):
        return f"<class Garage {self.cars}>"
    
    def __str__(self):
        return f"A garage with {len(self.cars)} cars"

garage = Garage()
garage.cars.append("Citroen")
garage.cars.append("Mazda")

print(garage.cars)

print(len(garage)) # 2

print(garage[0]) # Citroen

print(garage) # A garage with 2 cars