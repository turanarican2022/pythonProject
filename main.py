# FLOOR DIVISION
print(8/3) # 2.6666666666666665
print(8//3) # 2

# STRING CONCATENATION
print("Py" "thon") # Python
print("Py", "thon") # Py thon

# STRING SLICING
str = "some string"
print(str[0:4]) # some
print(str[5:]) # string
print(str[-6:-3]) # str
# Attempting to use an index that is too large will result in an error:
# print(str[34])
# However, out of range slice indexes are handled gracefully when used for slicing:
print(str[32:]) # ''
# strings are immutable: str[0] = "d" ---> error!
# length of a string
print(len(str)) # 11

# LISTS - SIMILAR TO ARRAYS OF OTHER LANGUAGES
cars_i_had = ["Citroen","Alfa Romeo","Mazda","Fiat"]
print(cars_i_had)
# slicing returns a new list
some_cars_i_had = cars_i_had[2:] # ['Citroen', 'Alfa Romeo', 'Mazda', 'Fiat']
print(some_cars_i_had) # ['Mazda', 'Fiat']
# so we can create a "shallow copy" of a list by this
cars_copied = cars_i_had[:]
print(cars_copied) # ['Citroen', 'Alfa Romeo', 'Mazda', 'Fiat']
# list concatenation
numbers = [4,5,6]
numbers_extended = [1,2,3] + numbers + [7,8,9]
print(numbers_extended) # [1, 2, 3, 4, 5, 6, 7, 8, 9]
# unlike strings (which are immutable), lists are mutable
cars_i_had[2] = "Mazda 323"
print(cars_i_had) # ['Citroen', 'Alfa Romeo', 'Mazda 323', 'Fiat']
# appending to the end of a list
numbers_extended.append(10)
print(numbers_extended) # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# replacing some values of a list
numbers_extended[3:6] = ["four","five","six"]
print(numbers_extended) # [1, 2, 3, 'four', 'five', 'six', 7, 8, 9, 10]
# emptying an array
numbers_extended[:]=[]
print(numbers_extended) # []
# nested lists
nested_lists = [["a","b","c",[1,2,3]],"x","y","z"]
print(nested_lists[0][3][1]) # 2
# end with a chosen string
i = 0
while i<10:
    print(f"a-{i}",end="***\n")
    i+=1
# a-0***
# a-1***
# a-2***
# a-3***
# a-4***
# a-5***
# a-6***
# a-7***
# a-8***
# a-9***