# Exceptions
'''
An exception is an event, which occurs during the execution of a program that disrupts the normal 
flow of the program's instructions
'''

try:
    print (4 + "2")
except TypeError:
    print ("it´s a exception.")
else:
    print ("Not exception here")
finally:
    print ("This print is execute always.")

#
try:
    print (4 + "2")
except TypeError as error:
    print ("it´s a exception.")
    print (error) # unsupported operand type(s) for +: 'int' and 'str'
else:
    print ("Not exception here")
finally:
    print ("This print is execute always.")