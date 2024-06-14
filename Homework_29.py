
def squared(x):
    return x ** 2


def is_odd(x):
    return x % 2


list_1 = [1, 2, 5, 7, 12, 11, 35, 4, 89, 10]
list_2 = map(squared, filter(is_odd, list_1))
print(list(list_2))
