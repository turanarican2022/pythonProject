## DICTIONARIES

cars = {"citroen":2012,"alfa romeo":2008,"mazda":1996,"fiat":2004}
print(cars["citroen"]) # 2012

# tuple or list of dictionaries
cars = (
    {"brand":"Citroen","year":2012},
    {"brand":"Alfa Romeo","year":2008},
    {"brand":"Mazda","year":1996},
    {"brand":"Fiat","year":2005},
)
print(cars[1]["brand"]) # Alfa Romeo

# turn into dictionary
cars = [("Citroen",2012),("Mazda",1996)]
cars_dict = dict(cars)
print(cars_dict) # {'Citroen': 2012, 'Mazda': 1996}

cars = (("Citroen",2012),("Mazda",1996))
cars_dict = dict(cars)
print(cars_dict) # {'Citroen': 2012, 'Mazda': 1996}

cars = (["Citroen",2012],["Mazda",1996])
cars_dict = dict(cars)
print(cars_dict) # {'Citroen': 2012, 'Mazda': 1996}