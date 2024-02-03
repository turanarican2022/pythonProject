#####################################
# FIRST CLASS FUNCTIONS             #
#####################################

# functions can be assigned to variables

def greet(name):
    print(f"hello {name}")

hello = greet
hello("Tuğba") # hello Tuğba

# mapping functions to variables with dictionaries

functions = {
    "write_name" : lambda person: f'{person["name"]} is {person["age"]} years old',
    "write_car": lambda car,car_year: f"Her car is a {car} of {car_year} model year"
}

person = {
    "name":"Halide",
    "age":38,

}

car = {
    "car":"BMW",
    "car_year":2024,
}

def write_info():
    write_name_here = functions["write_name"]
    print(write_name_here(person))
    # Halide is 38 years old
    write_car_here = functions["write_car"]
    print(write_car_here(**car))
    # Her car is a BMW of 2024 model year
    
write_info()