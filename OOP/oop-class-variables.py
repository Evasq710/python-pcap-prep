class Dog():
    counter = 0
    __private_counter = 0

    def __init__(self, name, age):
        self.__name = name
        self.age = age
        Dog.counter += 1
        Dog.__private_counter += 1


my_pet1 = Dog('Teddy', 2)
my_pet2 = Dog('Foxy', 2)
my_pet3 = Dog('Luna', 2)

# All 4 prints show the same value, counter is a class variable
print(my_pet1.counter)
print(my_pet2.counter)
print(my_pet3.counter)
print(Dog.counter)

# "Private" class variables works in the same way as "private" instance variables
print("private:", Dog._Dog__private_counter)


# Only instance variables with __dict__
print(my_pet1.__dict__)

# Showing class variables
print(Dog.__dict__)


if hasattr(Dog, 'counter'):
    print("My Dog class has a counter, yey")
else:
    print("My Dog class does not have a counter")

if hasattr(my_pet1, 'counter'):
    print("My Dog class has a counter, yey (obtained through a Dog instance)")
else:
    print("My Dog class does not have a counter (consulting a Dog instance)")


# __name__

# Kind of useless here
print(Dog.__name__) # returns 'Dog'
# print(my_pet1.__name__) # Doesn't exist for instances

# A more interesting use
print(type(my_pet1)) # returns <class '__main__.Dog'>
print(type(my_pet1).__name__) # returns 'Dog'


# __moudule__
# returns the name of the module that contains the definition of the class

print(Dog.__module__) # returns __main__ because it is defined in the same file
print(my_pet1.__module__) # returns __main__ because it is defined in the same file
