#####################################
# THE zip() FUCNTION #
#####################################

# the zip() function

all_cars = ["Citroen","Alfa Romeo","Mazda","Fiat","AMI"]
year = [2012,2008,1996,2005,2024]
status = ("sold","wrecked","sold","sold","will be bought")

zipped = zip(all_cars,year,status)
print(zipped) # <zip object at 0x7f5c2986b6c0>

zipped = tuple(zipped) # zip creates a tuple
print(zipped)
# (
# ('Citroen', 2012, 'sold'), ('Alfa Romeo', 2008, 'wrecked'), 
# ('Mazda', 1996, 'sold'), ('Fiat', 2005, 'sold'), 
# ('AMI', 2024, 'will be bought')
# )

zipped = list(zipped)
print(zipped)
# [
# ('Citroen', 2012, 'sold'), ('Alfa Romeo', 2008, 'wrecked'), 
# ('Mazda', 1996, 'sold'), ('Fiat', 2005, 'sold'), 
# ('AMI', 2024, 'will be bought')
# ]

zipped = zip(all_cars,year)
zipped = dict(zipped)
print(zipped) # {'Citroen': 2012, 'Alfa Romeo': 2008, 'Mazda': 1996, 'Fiat': 2005, 'AMI': 2024}