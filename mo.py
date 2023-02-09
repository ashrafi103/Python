#1. Write two methods with the same name but different number of parameters of same type and call the methods
def rk(a, b):
    r = a * b
    print(r)
def rk(a, b, c):
    r = a * b * c
    print(r)
rk(4, 5, 9)
rk(1, 2)
#2.  Write two methods with the same name but different number of parameters of different data type and call the methods
def rk(a, b):
    r = a * b
    print(r)
def rk(a, b, c):
    r = a * b * c
    print(r)
rk(4, 5, "abc")
#3. Write two methods with the same name and same number of parameters of same type
def rk(a, b,c):
    r = a * b
    print(r)
def rk(a, b, c):
    r = a + b + c
    print(r)
rk(10, 5, 19)
