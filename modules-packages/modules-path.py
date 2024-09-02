import sys

# list of all locations that it checks for modules, in the order of the list
print(sys.path)

# adding a relative path just for this execution
sys.path.append('modules_own_module')
print(sys.path)

# No actually necessary if we use packages