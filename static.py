# 1. Define a static variable and access that through a class
class Python:
    static = 10


print(Python.static)

# 2. Define a static variable and access that through a instance
ins = Python()
print(ins.static)

# 3. Define a static variable and change within the instance
ins.static = 15
print(ins.static)
print(Python.static)

# 4. Define a static variable and change within the class
Python.static = 14
print(Python.static)