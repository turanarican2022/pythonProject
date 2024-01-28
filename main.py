#####################################
# THE enumerate() FUNCTION #
#####################################

# enumerate(iterable, start=0)
# iterable must be a sequence, an iterator, or some other object which supports iteration.
# join a number with each element of the iterable

cars = ["Citroen","Alfa Romeo","Mazda","Fiat"]
enumerated = enumerate(cars)
print(enumerated) # <enumerate object at 0x7f65c414f580>

enumerated = list(enumerated)
print(enumerated) # [(0, 'Citroen'), (1, 'Alfa Romeo'), (2, 'Mazda'), (3, 'Fiat')]

enumerated = dict(enumerate(cars,start=2012))
print(enumerated) # {2012: 'Citroen', 2013: 'Alfa Romeo', 2014: 'Mazda', 2015: 'Fiat'}

for year, car in enumerated.items():
    print(f"I used a {car} in year {year}")
#
# I used a Citroen in year 2012
# I used a Alfa Romeo in year 2013
# I used a Mazda in year 2014
# I used a Fiat in year 2015
#