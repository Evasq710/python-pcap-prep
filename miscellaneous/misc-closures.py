'''
CLOSURES
A closure is a nested function that remembers the values of the outer function
'''

def greet(text):
    
    # print_greet is a closure, because we are referencing a variable from the outer function
    # without the "text" reference, this would be just a nested function
    # the variables that the closure remember and that are not destroyed when ther outer function ends, are called FREE VARIABLES (like "text" in this example)
    def print_greet():
        print(text)
    
    return print_greet


say_hello = greet('Hello')

print(say_hello) #  <function greet.<locals>.print_greet at 0x0000018CE83BD300>
say_hello()