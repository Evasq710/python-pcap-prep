class Dog():
    def __init__(self, name, age):
        self.__name = name
        self.age = age
    
    def get_age(self):
        return self.age

my_pet = Dog('Teddy', 2)
print(my_pet.__dict__) # printing the instance variables, but not the methods, for this see opp-class-variables.py (Dog.__dict__)

if hasattr(my_pet, '__name'):
    print("My dog's name is", my_pet.__name)
else:
    print("My dog has no name apparently")
    print(my_pet._Dog__name) # __name is not 100% private. Python changed the name to _<class>__<private attr>
    # print(my_pet.__name) # AttributeError, __name doesn't exist


my_pet.__breed = 'Bulldog'
print(my_pet.__dict__) # __breed doesn't change, because it is an atributte that wasn't defined in the class constructor
