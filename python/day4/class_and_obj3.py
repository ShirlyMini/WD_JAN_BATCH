# obj---instance--instance method---instance var
# constructor---instance method---no return statement--__init__
# invoked at the time of obj creation


#destructor- destroy the obj/attr-__del__---instance method


# class myclass:
#     def __init__(self):
#         print("this is the constructor")
#
#     def func1(self):
#         print("this is func: inst method")
#
#     def __del__(self):# called at the end of obj by default
#         print("this is destructor")
#
# obj=myclass()

##################################################3
# instance var

class myclass:
    def __init__(self,a,b):#TypeError: myclass.__init__() missing 2 required positional arguments: 'a' and 'b'
        print(a,b)# a, b are instance variable
        print("this is the constructor")
        # convert to class var using self
        self.var1=a
        self.b=b

        # convert to class var using class name# not recommended
        # myclass.var2=a
        # myclass.c=b

    def func1(self):
        print("instance var", self.var1,self.b)
        print("this is func: inst method")

    @classmethod
    def func2(cls):
        # print("class var", cls.var2,cls.c)
        print("this is func: class method")

    @staticmethod
    def func3():
        # print("static var", myclass.var2, myclass.c)
        print("this is func: static method")


obj=myclass(100,30)
obj.func1()
obj.func2()
obj.func3()

obj1=myclass(17,30)
obj1.func1()

