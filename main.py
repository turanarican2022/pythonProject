# ELSE KEYWORD WITH LOOPS

car_production = ["ok","ok","ok","faulty","ok"]

for control_check in car_production:
    if control_check != "ok":
        print("faulty encountered...! Skipping")
        break
    print("car was built, shipping it")
else:
    print("all production was successful") # never runs
# 
# car was built, shipping it
# car was built, shipping it
# car was built, shipping it
# faulty encountered...! Skipping
# car was built, shipping it
#

# the else keywords runs only if the whole loop ran without break or error 
# during iterations

car_production = ["ok","ok","ok","ok","ok"]
for control_check in car_production:
    if control_check != "ok":
        print("faulty encountered...! Skipping")
        continue
    print("car was built, shipping it")
else:
    print("all production was successful")
#
# car was built, shipping it
# car was built, shipping it
# car was built, shipping it
# car was built, shipping it
# car was built, shipping it
# all production was successful
#