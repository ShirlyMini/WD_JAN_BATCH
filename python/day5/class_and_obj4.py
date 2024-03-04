class myclass1:
    var1="myclass1 class variable"

    def __init__(self, a,b):
        self.a=a
        self.b=b

    def func1(self):
        print(self.a, self.b)

    @classmethod
    def func2(cls):
        print(cls.var1)

    @staticmethod
    def func3(h,b):
        print(h*b)


obj1=myclass1(1,2)
obj1.func1()# ins
obj1.func2()
obj1.func3(2,3)
obj2=myclass1(10,20)
obj1.func1()
obj1.func2()
obj1.func3(21,31)
obj3=myclass1(12,22)
obj1.func1()
obj1.func2()
obj1.func3(25,35)


class myclass2:
    var1 = "myclass2 class variable"
    @classmethod
    def func2(cls):
        print(cls.var1)

obj=myclass2()
obj.func2()

obj1=myclass2()
obj1.func2()


# static utility file--- config
#class method#factory# setup and teardown

# class ts

# def tc1
# def tc2