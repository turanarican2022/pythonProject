# LIST COMPREHENSIONS

"""
List comprehensions provide a concise way to create lists. Common applications are to make new lists where each element is the result of some operations applied to each member of another sequence or iterable, or to create a subsequence of those elements that satisfy a certain condition.
"""

squares = []
for x in range(10):
    squares.append(x**2)
print(squares) # [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

squares_comprehension = [x**2 for x in range(10)]
print(squares_comprehension) # [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

names = ["Halit","Turan","Halide","Tuğba"]
greets = [f"hello {name}" for name in names]
for greet in greets:
    print(greet)
"""
hello Halit
hello Turan
hello Halide
hello Tuğba
"""

# list comprehensions with if
multiply_if_different = [x*y for x in [2,8,4] for y in [3,2,9] if x != y]
print(multiply_if_different) # [6, 18, 24, 16, 72, 12, 8, 36]

genders = ["male","female"]
different_halits = [(name,gender) for name in names for gender in [ genders[0] if name == "Halit" or name == "Turan" else "female"]]
print(different_halits) # [('Halit', 'male'), ('Turan', 'male'), ('Halide', 'female'), ('Tuğba', 'female')]

# Nested list comprehensions
matrix = [
    [1,2,3,4],
    [5,6,7,8],
    [9,10,11,12]
]
transpozed = [[row[i] for row in matrix] for i in range(4)]
print(transpozed)
#
# [
#     [1, 5, 9], 
#     [2, 6, 10], 
#     [3, 7, 11], 
#     [4, 8, 12]
# ]
#

# the del statement
list = [1,2,3,4,5,6,7,8,9]
del list[1]
print(list) # [1, 3, 4, 5, 6, 7, 8, 9]
del list[2:5]
print(list) # [1, 3, 7, 8, 9]
del list[:] # does the same as list.clear()
print(list) # []
del list # can also be used to delete the entire variable