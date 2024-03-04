class parent1:
    var1="parent1"
    var="parent1 var"
    def func1(self):
        print("this is the func1 from parent1 class")

class parent2:
    var2 = "parent2"
    var = "parent2 var"
    def func1(self):
        print("this is the func1 from parent2 class")

class child(parent2, parent1):# 1 child# 2 p1 # 3 p2
    # Method resolution order
    def func2(self):
        print("this is the func1 from child class")
        print(f"var1{self.var1} var2{self.var2} var {self.var}")
        print(f"using class name var {parent2.var} {parent1.var}")
        # self.func1()
        # parent1.func1()#TypeError: parent1.func1() missing 1 required positional argument: 'self'
        parent1.func1(self)
        parent2.func1(self)
        # self.func2()#RecursionError: maximum recursion depth exceeded while calling a Python object

obj=child()
obj.func2()