try:
    stream = open('animals.txt')
    print(stream.read(10)) # read the first 10 bytes
    print(stream.read(10)) # read the next 10 bytes
    print(stream.read(100000)) # don't raise any error
    print(stream.read(1)) # empty string
    stream.close()
except Exception as e:
    print(e.args)
    print(e)

# char by char
try:
    stream = open('animals.txt')
    counter = 0
    character = stream.read(1)
    while character != '':
        counter += 1
        print(character, end='-')
        character = stream.read(1)
    print()
    print('Characters:', counter, end='\n\n')
    stream.close()
except Exception as e:
    print(e.args)
    print(e)

# line by line
try:
    stream = open('animals.txt')
    counter = 0
    line = stream.readline()
    while line != '':
        counter += 1
        print(line, end='')
        line = stream.readline()
    print()
    print('Lines:', counter, end='\n\n')
    stream.close()
except Exception as e:
    print(e.args)
    print(e)

# lines in a list
try:
    stream = open('animals.txt')
    counter = 0
    lines = stream.readlines()
    print('LINES')
    print(lines)
    print()
    stream.close()
except Exception as e:
    print(e.args)
    print(e)


# line by line (THE BEST OPTION)
# with this method, Python closes the file when reaches EOF
try:
    stream = open('animals.txt')
    print(stream) # <_io.TextIOWrapper name='animals.txt' mode='r' encoding='cp1252'>
    for line in stream:
        print(line, end='')
except Exception as e:
    print(e.args)
    print(e)


