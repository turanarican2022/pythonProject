#######################################
# modules                             #
#######################################

import name_module
from car_module import return_car as rc

print(name_module.return_full_name("Halide","Tuğba"))
# Halide Tuğba

print(rc())
# once I had an Alfa Romeo

print(dir(name_module))
# ['__builtins__', '__cached__', '__doc__', '__file__', 
# '__loader__', '__name__', '__package__', '__spec__', 
# 'return_full_name']

print(name_module.return_full_name)
# <function return_full_name at 0x7fc290866170>

print(name_module.__name__)
# name_module

print(name_module.__file__)
# /home/dajjal/Desktop/pythonProject/name_module.py