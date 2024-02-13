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

doubles_or_thrices = list(map(lambda x: x*2 if x%2 == 0 else x*3,range(10)))

print(doubles_or_thrices)
# [0, 3, 4, 9, 8, 15, 12, 21, 16, 27]