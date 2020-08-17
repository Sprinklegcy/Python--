from functools import reduce

print(reduce(lambda x, y: x + y, [reduce(lambda x, y: x * y, list(range(1, i))) for i in range(2, int(input()) + 2)]))

# def multiply(a, b):
#     return a * b

# for i in range(2, 6):
#     print(reduce(lambda x, y: x * y, list(range(1, i))))


# print([reduce(lambda x, y: x * y, list(range(1, i))) for i in range(2, 6)])
# n = int(input()) + 1


## print(sum([fun(i) for i in range(1, n)]))
