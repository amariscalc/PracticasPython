# Classes

'''
It is a programming structure that allows you to define a set of methods and attributes 
that describe an object or entity.
'''
class PersonEmpty:
    pass # we need to put code inside the class so that no error, like a "pass"

class Person:
    def __init__(self,name,surname,dni,alias = "Default Alias"): # def init self == class constructors
        self.name = name
        self.surname = surname
        self.alias = alias
        self.__dni = dni # private properties
        self.fullname = "{} {} ({})".format(self.name,self.surname,self.alias)
    # A class may contain functions
    def walk (self):
        print("%s %s is walking now"%(self.name,self.surname))
    # A function that return the DNI (private atribute)
    def get_dni (self):
        return self.__dni
    # A function to modify the DNI value
    def set_dni (self,dni):
        self.__dni = dni

# Create a new person
first_p = Person ("Alberto", "Mariscal","12345678X")
print ("Name: %s. Surname: %s."%(first_p.name,first_p.surname))
first_p.walk()

# Create other person
second_p = Person ("José","Jiménez","12345678X","Pepe")
print ("Name: %s. Surname: %s. Alias: %s"%(second_p.name,second_p.surname, second_p.alias))
print ("The fullname is : %s"%(second_p.fullname))
print ("The DNI is: %s"%(second_p.get_dni()))

# Modify the DNI
second_p.set_dni(input("Please, set the new DNI: "))
print ("The new DNI is: %s"%(second_p.get_dni()))
