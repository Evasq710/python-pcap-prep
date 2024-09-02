import platform

# print(dir(platform))

# If "aliased" is true, the function will use aliases for
# various platforms that report system names which differ from
# their common names, e.g. SunOS will be reported as
# Solaris. The system_alias() function is used to implement
# this.

# Setting terse to true causes the function to return only the
# absolute minimum information needed to identify the platform.

# return OS, both aliased and terse are set to False by default
print(platform.platform()) # Windows-10-10.0.19045-SP0
print(platform.platform(aliased=True, terse=True)) # just Windows-10

# generic OS name
print(platform.system()) # Windows

# System's release version as a single string
print(platform.version()) # 10.0.19045

# generic name of the processor
print(platform.machine()) # AMD64

# real name of the processor
print(platform.processor()) # AMD64 Family 25 Model 80 Stepping 0, AuthenticAMD

# Python implementation
print(platform.python_implementation()) # CPython
# CPython is the default and most widely used implementation of the Python language, written in C

# Python's version as a 3-element tuple: (major part, minor part, patch)
print(platform.python_version_tuple()) # ('3', '12', '5')