#######################################
# filter() and map() with lambda      #
#######################################

cars = [{"Citroen":"sold"},{"Alfa Romeo":"wrecked"},{"Mazda":"sold"},{"Fiat":"wrecked and sold"}]
    
sold_cars = list(filter(lambda car : "sold" in car.values() ,cars))

print(sold_cars)
# [{'Citroen': 'sold'}, {'Mazda': 'sold'}]

cars_end = list(map(lambda car: f"{list(car.keys())[0]} is {list(car.values())[0]}" ,cars))

print(cars_end)
# ['Citroen is sold', 'Alfa Romeo is wrecked', 'Mazda is sold', 'Fiat is wrecked and sold']