#####################################
# SET AND DICTIONARY COMPREHENSIONS #
#####################################

# set comprehensions

all_cars = ["Citroen","Alfa Romeo","Mazda","Fiat","Citroen"]
only_cars = {car for car in all_cars}
print(only_cars) #{'Fiat', 'Mazda', 'Citroen', 'Alfa Romeo'}

# dictionary comprehensions

cars = ["Citroen","Alfa Romeo","Mazda","Fiat","AMI"]
status = ["sold","wrecked","sold","sold","yet to be bought"]
cars_status = {cars[i]:status[i] for i in range(len(cars))}
print(cars_status)
# {'Citroen': 'sold', 'Alfa Romeo': 'wrecked', 'Mazda': 'sold', 'Fiat': 'sold', 'AMI': 'yet to be bought'}