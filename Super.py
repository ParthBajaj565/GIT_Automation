class A:
    def feature1(self):
        print("features 1")

    def feature2(self):
        print("features 2")

class B(A):
    def feature3(self):
        print("features 3")

    def feature4(self):
        print("features 4")

class C(B):
    def feature5(self):
        print("features 5")

    def feature6(self):
        print("features 6")


a=A()
a.feature1()
b=B()
b.feature2()
c=C()
c.feature4()