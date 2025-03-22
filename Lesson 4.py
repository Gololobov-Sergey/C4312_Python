# print(100, 300, "mama", True, 3.1415926)

def func(a, *args):
    for arg in args:
        print(arg)

# func(100, 300, "mama", True, 3.1415926, 5555)
# func(800)

def func2(**kwargs):
    p = 0
    for key in kwargs:
       p += kwargs[key]
    return p

# print(func2(a=3, b=6, c=5, d=2, e=4, f=10))

def summ(*elem):
    s = 0
    for el in elem:
        s += el
    return s

print(summ(2))
print(summ(2, "5"))
print(summ(2,6,4))
print(summ(2,3,5,6,8,9,7,56,4,3))