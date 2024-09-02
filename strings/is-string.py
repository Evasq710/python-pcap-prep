print('Adrian'.isalnum()) # true
print('Adrian30'.isalnum()) # true
print('Adrian   '.isalnum()) # false
print('Adrian 30'.isalnum()) # false
print('Adrian_'.isalnum()) # false
print('Adrian'.isalpha()) # true
print('Adrian'.isdigit()) # false
print('Adrian'.isnumeric()) # false
print()
print('48'.isdigit()) # true
print('48'.isnumeric()) # true
print('48.0'.isdigit()) # false
print('48.0'.isnumeric()) # false
print()
# all false
print('-48'.isdigit()) 
print('-48'.isnumeric()) 
print('-48'.isdecimal()) 
print('-48.0'.isdigit()) 
print('-48.0'.isnumeric())
print('-48.0'.isdecimal())
print()
print(''.isspace()) # false
print(' '.isspace()) # true
print('\n'.isspace()) # true
print(' \n'.isspace()) #true
print('\t'.isspace()) # true
print('\r'.isspace()) # true