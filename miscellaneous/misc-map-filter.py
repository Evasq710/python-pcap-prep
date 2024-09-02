'''GENERATOR'''

def this_is_a_generator():
    for i in range(5):
        yield i

a = this_is_a_generator()

print(this_is_a_generator) # function
print(a) # generator object
print(next(a))
print(next(a))
print(next(a))
print(next(a))
print(next(a))
# print(next(a)) # StopIteration Exception
print()


'''ITERATOR'''

lambda_func = lambda i: i * 2
initial_list = [1, 2, 3, 4, 5]

# 1 way of going thru the iterator
map_result = map(lambda_func, initial_list)
print(map_result) # map object (iterator)
print(next(map_result))
print(next(map_result))
print(next(map_result))
print(next(map_result))
print(next(map_result))
# print(next(map_result)) # StopIteration Exception

# Best way to go thru an iterator
map_result = map(lambda_func, initial_list)
for element in map_result:
    print(element, end=',')
print(end='\n\n')

# Putting all the elementos from an iterator into a new list
map_result = map(lambda_func, initial_list)
result_list = list(map_result)
print(result_list)

# This will return an empty list, because the whole iterator was already used
result_list2 = list(map_result)
print(result_list2)
print()

# a simplified way of doing this
print(list(map(lambda i: i * 2, [1, 2, 3, 4, 5])))
print()


'''FILTER'''
# Checking if the elements are even numbers
print(list(filter(lambda i: i % 2 == 0, [1, 2, 3, 4, 5])))
print()