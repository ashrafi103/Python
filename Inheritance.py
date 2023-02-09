class A():
    def display(self):
            print("Display Inside class A ")
    def show(self):
            print("Show Inside class A")
    def print1(self):
            print(" this is overrding method")
class B (A):
    def display2(self):
            print("Display Inside class B ")
    def show2(self):
            print("Show Inside class B")
    def print1(self):
            print(" this is overrding method OF A")
class C (B):
    def display3(self):
            print("Display Inside class C ")
    def show3(self):
            print("Show Inside class C")
    def print1(self):
            print(" this is overrding method OF A1")
s=A()
s.show()
s.display()
s.print1()
d=B()
d.show2()
d.display2()
d.print1()

g=C()
g.display3()
g.show3()
g.print1()
