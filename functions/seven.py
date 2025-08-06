def add(*args):
    # print(args)
    res = 0
    for i in args:
        res = i+res
    return res

print(add(2,4,5,6))