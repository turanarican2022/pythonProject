# DESTRUCTURING SYNTAX
cars = ["Citroen","Alfa Romeo","Mazda","Fiat"]
car1, car2, car3, car4 = cars
print(car1, car2, car3, car4) # Citroen Alfa Romeo Mazda Fiat

cars = ("Citroen","Alfa Romeo","Mazda","Fiat")
car1, car2, car3, car4 = cars
print(car1, car2, car3, car4) # Citroen Alfa Romeo Mazda Fiat

cars = {"Citroen","Alfa Romeo","Mazda","Fiat"}
car1, car2, car3, car4 = cars
print(car1, car2, car3, car4) # Mazda Alfa Romeo Citroen Fiat (or any other order)

cars = [("Citroen",2012),("Alfa Romeo",2008),]
car1, car2 = cars
print(car1,car2) # ('Citroen', 2012) ('Alfa Romeo', 2008)
print(car1[0],car1[1],car2[0],car2[1]) # Citroen 2012 Alfa Romeo 2008

for car,year in cars:
    print(f"{car} is made in {year}")
    #
    # Citroen is made in 2012
    # Alfa Romeo is made in 2008
    #
for car_tuple in cars:
    print(f"{car_tuple[0]} was made in {car_tuple[1]}")
    #
    # Citroen was made in 2012
    # Alfa Romeo was made in 2008
    #
    
cars = (("Citroen",2012),("Alfa Romeo",2008),)
for car,year in cars:
    print(f"{car} is made in {year}")
    #
    # Citroen is made in 2012
    # Alfa Romeo is made in 2008
    #
    
cars = {("Citroen",2012),("Alfa Romeo",2008),}
for car,year in cars:
    print(f"{car} is made in {year}")
    #
    # Alfa Romeo is made in 2008
    # Citroen is made in 2012
    #
    
cars = (("Citroen",2012,"sold"),("Alfa Romeo",2008,"wrecked"),)
for car,year,end in cars:
    print(f"{car} was made in {year} and in the end it is {end}")
    #
    # Citroen was made in 2012 and in the end it is sold
    # Alfa Romeo was made in 2008 and in the end it is wrecked
    #

cars = {"Citroen":(2012,"sold"),"Alfa Romeo":(2008,"wrecked")}
for car,(year,end) in cars.items():
    print(f"{car} was made in the year {year} and in the end it is {end}")
    #
    # Citroen was made in the year 2012 and in the end it is sold
    # Alfa Romeo was made in the year 2008 and in the end it is wrecked
    #
    