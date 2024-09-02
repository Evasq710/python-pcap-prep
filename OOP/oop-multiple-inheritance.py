'''
Python's MRO (Method Resolution Order):
1. Look inside the object
2. If not found, look in the supperclasses from left to right
3. If not found, show an error
'''

class Vehicle():
    def go(self):
        print('Going!')
    
    def introduce(self):
        print('I am a Vehicle')

class Flyable():
    def fly(self):
        print('Flying!')
    
    def introduce(self):
        print('I am a Flyable')
    
    def call_introduce_from_flyable(self):
        self.introduce()

class Airplane(Vehicle, Flyable): # Try changing this order
    pass

my_plane = Airplane()
print(Airplane.__dict__)
my_plane.go()
my_plane.fly()
my_plane.introduce() # 'I am a Vehicle'
my_plane.call_introduce_from_flyable() # Although this method is inside Flyable, the <self> reference makes it to follow the Python's MRO, so we see 'I am a Vehicle'