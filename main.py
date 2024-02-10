#######################################
# dictionary comprehension            #
#######################################

cars = {"Citroen":34000,"Alfa Romeo":28000,"Mazda":6000,"Fiat":18000}

cars_in_eu = {car:price/2 for (car,price) in cars.items()}

print(cars_in_eu)
# {'Citroen': 17000.0, 'Alfa Romeo': 14000.0, 'Mazda': 3000.0, 'Fiat': 9000.0}

cheap_cars = {car:price for (car,price) in cars.items() if price<20000}

print(cheap_cars)
# {'Mazda': 6000, 'Fiat': 18000}

cars = {car:("cheap" if price <20000 else "expensive") for (car,price) in cars.items()}

print(cars)
# {'Citroen': 'expensive', 'Alfa Romeo': 'expensive', 'Mazda': 'cheap', 'Fiat': 'cheap'}