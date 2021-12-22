def itay(ls, func1, func2):
    for i in range(len(ls)):
        if ls[i] % 2 == 0:
            ls[i] = (func1(ls[i]))
        else:
            ls[i] = (func2(ls[i]))
    print(ls)

itay([2, 2, 3], lambda x: x ** 2, lambda x: x + 1)
