
class Vehicle(object):
    """docstring"""

    def __init__(self, color, doors, tires, vtype):
        """Constructor"""
        self.color = color
        self.doors = doors
        self.tires = tires
        self.vtype = vtype

    def brake(self):
        """
        Stop the car
        """
        return "%s braking" % self.vtype

    def drive(self):
        """
        Drive the car
        """
        return "I'm driving a %s %s!" % (self.color, self.vtype)

if __name__ == "__main__":
    car = Vehicle("blue", 5, 4, "car")
    print(car.brake())
    print(car.drive())

    truck = Vehicle("red", 3, 6, "truck")
    print(truck.drive())
    print(truck.brake())



print('-------------------------------------------------------------------')    

class Car(Vehicle):
    """
    The Car class
    """

    #----------------------------------------------------------------------
    def brake(self):
        """
        Override brake method
        """
        return "The car class is breaking slowly!"

if __name__ == "__main__":
    car = Car("yellow", 2, 4, "car")

    print(car.brake())
    # 'The car class is breaking slowly!'

    print(car.drive())
    # "I'm driving a yellow car!"


# Using the default values of the parent class is known as inheriting or inheritance. 
# This is a big topic in Object Oriented Programming (OOP). 
# This is also a simple example of polymorphism.
# Polymorphic classes typically have the same interfaces (i.e. methods, attributes), 
# but they are not aware of each other.
# In Python land, polymorphism isn’t very rigid about making sure the interfaces are exactly 
# the same. Instead, it follows the concept of duck typing. 
# The idea of duck typing is that if it walks like a duck and talks like a duck, 
# it must be a duck. So in Python, as long as the class has method names that are the same, 
# it doesn’t matter if the implementation of the methods are different.    