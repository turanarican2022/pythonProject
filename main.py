####################################################
# reading from and writing to csv files            #
# to Joshua...

import csv

with open("read.csv", newline="") as read:
    parsed_read = csv.DictReader(read)
    for person in parsed_read:
        print(
            f'{person["name"]} is {person["age"]} years old and lives in {person["country"]}')
        # Halit is 38 years old and lives in Turkey
        # Nitissa42 is Spain years old and lives in None
        # Ammar is 23 years old and lives in Pakistan

# reading with a different "delimiter"(seperator):
with open("read_sep_.csv", newline="") as read_sep:
    parsed_read = csv.DictReader(read_sep, delimiter=";")
    for customer in parsed_read:
        print(
            f'{customer["customer"]} lives at address: {customer["address"]}')
        # Amiran Temerris lives at address:  73498, LA, US
        # Mick Mo lives at address:  DK, COP, 34, TF St.


cars = [{"brand": "Citroen", "model": "C3", "year": 2012},
        {"brand": "Alfa Romeo", "model": "156", "year": 2008}]

with open("write.csv", "w") as write:
    field_names = ["brand", "model", "year"]
    write_to = csv.DictWriter(write, fieldnames=field_names)
    write_to.writeheader()
    for car in cars:
        write_to.writerow(car)

# confirm writing

with open("write.csv") as confirm:
    cars = csv.DictReader(confirm)
    for car in cars:
        print(f'{car["brand"]} {car["model"]} was made in {car["year"]}')
        # Citroen C3 was made in 2012
        # Alfa Romeo 156 was made in 2008

# writing with a different "delimiter"(seperator):

with open("write_sep_.csv", "w") as write_sep:
    field_names = ["brand", "model", "year"]
    write_to_sep = csv.DictWriter(
        write_sep, fieldnames=field_names, delimiter=";")
    write_to_sep.writeheader()
    write_to_sep.writerow({"brand": "Citroen", "model": "C3", "year": 2012})
