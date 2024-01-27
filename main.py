cars = {"Citroen":(2012,"sold"),"Alfa Romeo":(2008,"wrecked")}

for car in cars: # to iterate over keys
    print(car)
    # Citroen
    # Alfa Romeo

for (year,end) in cars.values(): # to iterate over values
    print(f"built in {year} and later {end}")
    # built in 2012 and later sold
    # built in 2008 and later wrecked

for car,(year,end) in cars.items(): # to iterate over items
    print(f"{car} was made in the year {year} and in the end it is {end}")
    #
    # Citroen was made in the year 2012 and in the end it is sold
    # Alfa Romeo was made in the year 2008 and in the end it is wrecked
    #