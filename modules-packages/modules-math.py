import math

# print(dir(math))

print("ceil")
print(math.ceil(3.6)) # round up > 4
print(math.ceil(3.1)) # round up > 4
print(math.ceil(-3.6)) # round up > -3
print(math.ceil(-3.1), end='\n\n') # round up > -3

print("floor")
print(math.floor(3.6)) # round down > 3
print(math.floor(3.1)) # round down > 3
print(math.floor(-3.6)) # round down > -4
print(math.floor(-3.1), end='\n\n') # round down > -4

print("trunc")
print(math.trunc(3.6)) # trunc > 3
print(math.trunc(3.1)) # trunc > 3
print(math.trunc(-3.6)) # trunc > -3
print(math.trunc(-3.1), end='\n\n') # trunc > -3
# Same effect with int()
print(int(3.6)) # trunc > 3
print(int(3.1)) # trunc > 3
print(int(-3.6)) # trunc > -3
print(int(-3.1), end='\n\n') # trunc > -3

print("factorial")
print(math.factorial(4), end='\n\n')
# print(math.factorial(-4)) # ValueError

print("sqrt")
print(math.sqrt(16), end='\n\n') # FLOAT

print("hypot")
print(math.hypot(3, 4))
print(math.sqrt(3**2 + 4**2)) # same answer as in hypot > 5.0