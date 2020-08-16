#Everything in Python is an object. 
# That’s a very vague statement unless you’ve taken a computer programming class or two. 
# What this means is that every thing in Python has methods and values. 
# The reason is that everything is based on a class. A class is the blueprint of an object. 
# Let’s take a look at what I mean:

# It means that a string is based on a class and x is an instance of that class!
x = "Mike"
attrs = dir(x)
print(attrs)


# You may be wondering why I keep saying method instead of function. 
# A function changes its name to “method” when it is within a class. 
# You will also notice that every method has to have at least one argument (i.e. self), 
# which is not true with a regular function.

# In Python 3, we don’t need to explicitly say we’re inheriting from object. 
# Instead, we could have written the above like this:

print('------------------------------------------------------------------------------------------')

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