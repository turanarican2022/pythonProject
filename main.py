# LISTS, TUPLES, SETS


# LISTS

cars = [["Citroen","C3",2012],["Alfa Romeo","156",2008],["Mazda","323",1996]]
print(cars[0][2]) # 2012

# append()
cars.append(["Fiat","Marea",2005])
print(cars[len(cars)-1][0]) # Fiat

#remove()
cars.remove(cars[0])
print(cars) # [['Alfa Romeo', '156', 2008], ['Mazda', '323', 1996], ['Fiat', 'Marea', 2005]]


# TUPLES

not_a_tuple = "Citroen"
a_turple = "Citroen",
print(type(a_turple)) # <class 'tuple'>
a_not_prefered_tuple_expression = "Citroen","Alfa Romeo"
print(type(a_not_prefered_tuple_expression)) # <class 'tuple'>
a_clear_tuple = ("Mazda","Fiat")
print(type(a_clear_tuple)) # <class 'tuple'>

# append() cannot be used with tuple, instead
joined_tuple = ("Citroen",) + ("Alfa Romeo",) + a_clear_tuple +("MG",) 
print(joined_tuple) # ('Citroen', 'Alfa Romeo', 'Mazda', 'Fiat', 'MG')


# SETS
# sets are unordered and contains only unique values

cars = {"Citroen","Alfa Romeo","Mazda","Fiat"}
print(cars) # {'Fiat', 'Citroen', 'Mazda', 'Alfa Romeo'}

# add to a set
cars.add("MG")
print(cars) # {'Citroen', 'MG', 'Mazda', 'Alfa Romeo', 'Fiat'}

# remove from a set
cars.remove("MG")
print(cars) # {'Citroen', 'Fiat', 'Mazda', 'Alfa Romeo'}

science_friends = {"Jane","Bob","Rob"}
art_friends = {"Tina","Jane"}

# difference of sets
science_but_not_art = science_friends.difference(art_friends)
print(science_but_not_art) # {'Bob', 'Rob'}

# symmetric difference (not included in both at the same time)
not_in_both = science_friends.symmetric_difference(art_friends)
print(not_in_both) # {'Bob', 'Rob', 'Tina'}

# intersection (present in both)
present_in_both = science_friends.intersection(art_friends)
print(present_in_both) # {'Jane'}

# union (present in both but without duplication)
union = science_friends.union(art_friends)
print(union) # {'Rob', 'Tina', 'Jane', 'Bob'}
