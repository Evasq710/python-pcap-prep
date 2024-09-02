try:
    stream = open('newfile.txt', 'w') # if the file doesn't exist, python creates it
    stream.write('First message\n')
    stream.write('Second message\n')
    stream.close()
except Exception as e:
    print(e)

try:
    stream = open('newfile.txt', 'w')
    stream.write('This is a brand new message\n') # deletes the previous content of the file
    stream.close()
except Exception as e:
    print(e)