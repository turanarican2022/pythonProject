#######################################
# filter() and map() with lambda      #
#######################################

cars = [{"Citroen":"sold"},{"Alfa Romeo":"wrecked"},{"Mazda":"sold"},{"Fiat":"wrecked and sold"}]
    
sold_cars = list(filter(lambda car : "sold" in car.values() ,cars))

print(sold_cars)

cars_end = list(map(lambda car: f"{list(car.keys())[0]} is {list(car.values())[0]}" ,cars))

print(cars_end)