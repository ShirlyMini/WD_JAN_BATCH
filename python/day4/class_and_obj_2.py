# 4 types of variable
# local
# global
# class
# instance

# globalvar="global_var"
# class myclass:
#     classvar="class_var"
#     def myfunc(self, a, b):# a,b,c are local var
#         c=10
#         print(f"a:{a} b:{b} c:{c} \nclassvar with classname:{myclass.classvar}"
#               f"\nclassvar with self/[obj]:{self.classvar}"
#               f"\nglobalvar:{globalvar}")
#
# obj=myclass()
# obj.myfunc(1,2)


#################################################################333333333333

var="global_var"
class myclass:
    var="class_var"
    def myfunc(self):
        var=10
        print(globals())# dict
        print(f"var:{var} \nclassvar with classname:{myclass.var}\nclassvar with self:{self.var}\n"
              f"globalvar:{globals().get('var')}")
        return var

    @classmethod
    def func2(cls):
        var=20
        print(cls==myclass)#True
        print(f"var:{var} \n"
              f"classvar with classname:{myclass.var}\n"
              f"classvar with cls:{cls.var}\n"
              f"globalvar:{globals().get('var')}")
        return var

    @staticmethod
    def func3():
        var=30
        print(f"var:{var} \n"
              f"classvar with classname:{myclass.var}\n"
              f"globalvar:{globals().get('var')}")
        return var



# obj=myclass()
# # obj.myfunc()
# print(var)# global
# print(obj.var)# class
# print(myclass.var)# class
# print(obj.myfunc())# get local

# myclass.func2()
# print(var)# global
# print(myclass.var)# class
# print(myclass.func2())# get local

# print(myclass.func3())# get local

