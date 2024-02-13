#######################################
# set methods                         #
#######################################

set_1 = {"Nitissa","Aisis","Adissas","Nita","Arin"}
set_2 = {"Nitissa","Nita","Tamara","Jacob"}

# union:
print(set_1 | set_2)
print(set_1.union(set_2))
# {'Tamara', 'Nita', 'Nitissa', 'Arin', 'Aisis', 'Adissas', 'Jacob'}

# intersection
print(set_1&set_2)
print(set_1.intersection(set_2))
# {'Nitissa', 'Nita'}

# difference
print(set_1-set_2)
print(set_1.difference(set_2))
# {'Arin', 'Aisis', 'Adissas'}

# symmetric difference - elements that do not belong to the both sets at the same time
print(set_1^set_2)
print(set_1.symmetric_difference(set_2))
# {'Arin', 'Aisis', 'Jacob', 'Tamara', 'Adissas'}