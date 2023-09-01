# List Comprehension

'''
List comprehension in Python is an easy and compact syntax for creating a list from a string or another list. 
It is a very concise way to create a new list by performing an operation on each item in the existing list. 
List comprehension is considerably faster than processing a list using the for loop.
'''
# Create a list. The list contain "n" elements in range
my_first_list = [i for i in range(8)] 
my_list = [i for i in range(27,35)]

# Other create list method
my_original_list = range (8)

print (list(my_original_list)) # [0, 1, 2, 3, 4, 5, 6, 7]
print (my_list) # [27, 28, 29, 30, 31, 32, 33, 34]

# Operator in the for bucle
my_other_list = [i*2 for i in range(8)]
print (my_other_list) # [0, 2, 4, 6, 8, 10, 12, 14]

import math
my_other_list = [ i * math.pi for i in range(5)]
print (my_other_list) # [0.0, 3.141592653589793, 6.283185307179586, 9.42477796076938, 12.566370614359172]

# Functions in the for bucle
def sum_pi (num):
    return num + math.pi

my_other_list = [ sum_pi(i) for i in range(4)]
print (my_other_list) # [3.141592653589793, 4.141592653589793, 5.141592653589793, 6.141592653589793]