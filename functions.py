a = int(input("insert length: "))
b = int(input("insert breadth: "))
def area(a,b):
    return a*b
print("Area is ",area(a,b))

#define a function with unlimited arguments
def mean(*args):
    return args/len(args)

#define function with indefinite keyword arguments
def mean(**kwargs):
    return kwargs/len(kwargs)