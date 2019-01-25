def mult_func(n):
    return lambda a : a * n
doubler = mult_func(2)
tripler = mult_func(3)
print(doubler(11))
print(tripler(11))