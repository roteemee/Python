def func1(list):
    new_tmp = [x for x in list if type(x) == int ]
    return new_tmp

def func2(list):
    new_tmp = [x if type(x) == int else 0 for x in list ]
    return new_tmp

def func3(list):
    return sum([float(x) for x in list])


print(sum([1,2,3,4 ]))
