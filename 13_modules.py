# Modules

'''
it´s a file containing Python definitions and statements.
A module can define functions, classes, and variables. A module can also include runnable code. 
Grouping related code into a module makes the code easier to understand and use. 
It also makes the code logically organized.
More info:
https://www.geeksforgeeks.org/python-modules/
'''

# Import all file´s data
import module_calc # import all data of module_calc.py

#module_calc.main_calc()

# Import only a function
# Import only "sum" function of "module_example"
from module_example import sum

#numbers = module_calc.set_numbers()
#print("El resultado es %d"%(sum (numbers [0],numbers[1])))


# Example math module
import math # import all data of module math (included in python installation)

number_a = float (40)

x = math.log10(number_a)
print (x) # 1.6020599913279623

pi = math.pi
print (pi) # 3.141592653589793
print (math.pow(3,3)) # 27.0

# Import only a funct as alias
from math import cos as cosine_value
print (cosine_value(pi)) # -1.0