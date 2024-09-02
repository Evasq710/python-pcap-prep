class Vehicle:
    class_message = 'This is a message from the Vehicle class'

    def __init__(self, speed):
        self.speed = speed

class LandVehicle(Vehicle):
    def __init__(self, speed, wheel_count):
        # Vehicle.__init__(self, speed) # another way that needs the self parameter
        super().__init__(speed)
        self.wheel_count = wheel_count
        # print(Vehicle.class_message)
        print(super().class_message)
    
    def speed_up(self):
        self.speed += 5

class Car(LandVehicle):
    def super_speed(self):
        print('Super speed activated!')
        super().speed_up()
        super().speed_up()
        super().speed_up()


my_car = Car(5, 4)
print(Car.__dict__)

print()
print(my_car.__dict__)
my_car.super_speed()
print(my_car.__dict__)
my_car.speed_up()
print(my_car.__dict__)

print()
print(isinstance(my_car, Car)) # True
print(isinstance(my_car, LandVehicle)) # True
print(isinstance(my_car, Vehicle)) # True

print()
print(issubclass(Car, LandVehicle)) # True
print(issubclass(Car, Vehicle)) # True
print(issubclass(Car, Car)) # True
print(issubclass(LandVehicle, Vehicle)) # True

print()
print(issubclass(LandVehicle, Car)) # False
print(issubclass(Vehicle, Car)) # False


## IS operator

# OBJECTS

my_new_car = my_car
print()
print(my_new_car is my_car) # True

my_third_car = Car(5, 4)
print(my_new_car is my_third_car) # False
print()

# NUMS
first_num = 5
secont_num = 5
print(first_num is secont_num) # True

first_num = 5
secont_num = 5.0
print(first_num is secont_num) # False
print(first_num == secont_num) # True

first_num = 5
secont_num = 2
secont_num += 3
print(first_num is secont_num) # True
print()

# STRINGS
first_str = 'hello'
second_str = 'hello'
print(first_str is second_str) # True

first_str = 'hello'
second_str = 'hell'
second_str += 'o'
print(first_str is second_str) # False
print(first_str == second_str) # True
print()



