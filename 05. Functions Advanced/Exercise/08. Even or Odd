def even_odd(*args):
    command = args[-1]
    numbers = args[:-1]

    if command == "even":
        return list(filter(lambda num: num % 2 == 0, numbers))
    if command == "odd":
        return list(filter(lambda num: num % 2 == 1, numbers))


print(even_odd(1, 2, 3, 4, 5, 6, "even"))
print(even_odd(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, "odd"))
