def sum(a, b):
    return a + b

# a lambda function (or annonymus function) doesn't have a name, and can only have 1 instruction
another_sum = lambda a, b: a + b

print(sum(5, 3))
print(sum)
print(another_sum(5, 3))
print(another_sum)


# a lambda application

def apply_lambda_func(elements: list, func) -> None:
    for element in elements:
        print(f'{element}:', func(element))

my_func = lambda x: x * x
apply_lambda_func([1, 2, 3, 4, 5], my_func)
print()

apply_lambda_func([1, 2, 3, 4, 5], lambda x: 1 / x)
print()

apply_lambda_func([1, 2, 3, 4, 5], lambda x: x ** x)
print()