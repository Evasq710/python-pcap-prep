print('work work work'.find('work')) # 0
print('work work work'.rfind('work')) # 10

print()
print('work work work'.find('work', 2)) # 5
print('work work work'.rfind('work', 2)) # 10

print()
print('work work work'.find('work', 2, 5)) # -1
print('work work work'.rfind('work', 2, 5)) # -1

print()
print('work work work'.rfind('work', 0, 5)) # 0
print('work work work'.find('work', 0, 5)) # 0