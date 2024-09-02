import random

# If we don't specify a sedd, python does it for us, choosing the time of the computer as the seed
# Setting a specific seed will lead to the same "random" number every time we run the script
# random.seed(0)
print(random.random())
print(random.random())
print(random.random())


numbers = [1, 2, 3, 4, 5, 6]
for i in range(len(numbers)):
    print(random.choice(numbers)) # it is possible that we get duplicate results

print(random.choice('SomeString'))


names = ['a', 'b', 'c', 'd', 'e']
print(random.sample(names, 3)) # will return a list with 3 unique random values from names (unique indexes, it doesn't validate if the values ar unique)



print()
print('### EXERCISE ###') 
def generate_tickets(ticket_count, max_number):
    import random
    # from range(0, max_number), we ar getting a random sample of ticket_count elements
    list_to_return = random.sample(range(0, max_number), ticket_count)
    # another way of doing it
    # list_to_return = random.sample([i for i in range(0, max_number)], ticket_count)

    # we return that list, and the random winner
    return (list_to_return, random.choice(list_to_return))
    # another way of doing it, using a sample of 1 element
    # return (list_to_return, random.sample(list_to_return, 1)[0])


print(generate_tickets(5, 10))