# class parent1:
#     var1="parent1"
#     var="parent1 var"
#     def func1(self):
#         print("this is the func1 from parent1 class")
#
# class parent2:
#     var2 = "parent2"
#     var = "parent2 var"
#     def func1(self):
#         print("this is the func1 from parent2 class")
#
# class child(parent2, parent1):# 1 child# 2 p1 # 3 p2
#     # Method resolution order
#     var="child var"
#     def func2(self):
#         print("this is the func1 from child class")
#         print(f"var1{self.var1} var2{self.var2} var {self.var}")# child and the to parent
#         print(f"using class name var {parent2.var} {parent1.var}")
#         print(super())#<super: <class 'child'>, <child object>>
#         print(super().func1())
#         print(super().var1)
#         print(super().var2)
#         print(super().var)#will take the parent classes
#         # self.func1()
#         # parent1.func1()#TypeError: parent1.func1() missing 1 required positional argument: 'self'
#         # parent1.func1(self)
#         # parent2.func1(self)
#         # self.func2()#RecursionError: maximum recursion depth exceeded while calling a Python object
#
# obj=child()
# obj.func2()


#######################################################################3

#


class parent1:
    def __init__(self, a, b):
        print("this is parent1 constructor")
        self.a1=a
        self.b1=b

class parent2:
    def __init__(self, a, b):
        print("this is parent2 constructor")
        self.a2=a
        self.b2=b

    @classmethod
    def class_func(cls):
        print("this is class func of parent2")

    @staticmethod
    def static_func():
        print("this is static func of parent2")

class child(parent1, parent2):# MRO
    def __init__(self, a, b, c,d,e,f):
        print("this is child constructor")
        parent1.__init__(self, c, d)
        parent2.__init__(self, e, f)
        self.a=a
        self.b=b

        # super().__init__()

    def func1(self):
        print("instance var of child", self.a, self.b)
        print("instance var of parent1", self.a1, self.b1)
        print("instance var of parent2", self.a2, self.b2)
        self.class_func()
        self.static_func()

        parent2.class_func()
        parent2.static_func()
    # pass


obj=child(1,2, 3,4,5,6)
obj.func1()



