#####################################
# FUNCTIONS #
#####################################

cars = [{"make":"Citroen","year":2012},{"make":"Alfa Romeo","year":2008}]

def print_car(car):
    print(f'{car["make"]} was built in {car["year"]}')
    
print_car(cars[0]) # Citroen was built in 2012
print_car(cars[1]) # Alfa Romeo was built in 2008

# returning functions

def return_car(make,model):
    return f"{make} {model}"

print(return_car("Fiat","Marea")) # Fiat Marea

# named arguments
# !!! if one of the arguments is named, all the subsquent arguments must be named
# !!! a named argument must come after an unnamed argument

print(return_car(make="Mazda",model="323")) # Mazda 323
# print(return_car(make="Citroen","C3")) ---> not allowed

# default parameters
# !!! if one of the parameters has a default value, all the subsequent parameters must allso have
# !!! a parameter with a default value must come after parameters without default values

def return_name(name,sur_name="ARICAN"):
    return f"{name} {sur_name}"

print(return_name("Halit")) # Halit ARICAN
print(return_name("Halide","Tuğba")) # Halide Tuğba
print(return_name("Halide",sur_name="Tuğba")) # Halide Tuğba