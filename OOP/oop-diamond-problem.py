'''
Python's MRO (Method Resolution Order):
1. Look inside the object
2. If not found, look in the supperclasses from left to right
3. If not found, show an error
'''

class Vehicle():
    def show_power_type(self):
        print('Various sources')

class ElectricVehicle(Vehicle):
    def show_power_type(self):
        print('Electricity')

class PetrolVehicle(Vehicle):
    def show_power_type(self):
        print('Petrol')

class HybridCar(ElectricVehicle, PetrolVehicle):
    pass

my_hybrid = HybridCar()
my_hybrid.show_power_type()