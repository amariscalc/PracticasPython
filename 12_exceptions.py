# Exceptions
'''
An exception is an event, which occurs during the execution of a program that disrupts the normal 
flow of the program's instructions
'''

try:
    print (4 + "2")
except TypeError as error_type_error:
    print ("it´s a exception. {}".format(error_type_error)) # it´s a exception. unsupported operand type(s) for +: 'int' and 'str'
else:
    print ("Not exception here")
finally:
    print ("This print is execute always.")

#
try:
    print (4 + "2")
except ValueError as error_value:
    print ("it´s a exception ValueError %s"%(error_value))
except Exception as error_exception:
    print ("it´s a exception. %s" %(error_exception)) # it´s a exception. unsupported operand type(s) for +: 'int' and 'str'
else:
    print ("Not exception here")
finally:
    print ("This print is execute always.")