# STRING FORMATTING

first_name = "Halit"
second_name = "Turan"
full_name = f"{first_name} {second_name} ARICAN"
print(full_name) # Halit Turan ARICAN

greet_person = "hello {}, how are you?"
greet_halit = greet_person.format("Halit")
print(greet_halit) # hello Halit, how are you?

greet_woman = "hello Ms. {name} {surname}, you should be happy."
greet_halide = greet_woman.format(name="Halide",surname="Tuğba")
print(greet_halide) # hello Ms. Halide Tuğba, you should be happy.