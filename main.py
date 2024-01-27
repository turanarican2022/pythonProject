# ELSE KEYWORD WITH LOOPS
# In a for loop, the else clause is executed after the loop reaches its final iteration.
# In a while loop, it’s executed after the loop’s condition becomes false.
# In either kind of loop, the else clause is not executed if the loop was terminated by a break.

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