# class - template or blueprint
#creation - no mem allocation- reference
# class attribute - var, method
# method- func defined in class
# empty class
# class myclass:
#     pass
#
# print(myclass)#<class '__main__.myclass'>

#
# obj - phy/real-time entity
# mem allocation
# instance creation/object creation/insanciation

###########################instance method

# class resume_template:
#
#     def func1(self, name, qual):
#         print(self)#<__main__.resume_template object at 0x000001844CD84210>
#         # 1. self repr the obj# self as coding standard
#         # 2. always it shoudl be passed as first parameter
#         print(f"name {name} \n Qualification {qual}")
#
#
#     def func2(self):
#         print("this is func2")

# stud1=resume_template()#insanciation
# stud1.func1("ram", "be")# passing the obj as first parameter
#
# stud2=resume_template()#insanciation
# stud2.func1("sam", "be")
# stud2.func2()
#
# print(resume_template())#<__main__.resume_template object at 0x000001A293F14150>
# print(resume_template)#<class '__main__.resume_template'>

# stud1=resume_template
# stud1.func1(stud1, "be", "None")
#
# stud2=resume_template
# stud2.func1(stud2, "be", "None")
# stud2.func2(stud2)


#####################################################################3

###########################class method

# class myclass:
#     @classmethod
#     def func1(cls, a, b):
#         print(cls)#<class '__main__.myclass'>
#         print(f"a {a} ,b {b}")
#
#     @classmethod
#     def func2(cls):
#         print("this is func2")
#
#
# ###############with obj
#
# obj=myclass()
# obj.func1(1,2)#
# #obj.func2()#TypeError: myclass.func2() takes 0 positional arguments but 1 was given
#
# ################with classname
# myclass.func1(1,2)#
# #myclass.func2()#TypeError: myclass.func2() takes 0 positional arguments but 1 was given

#####################################################################3

###########################static method

# class myclass:
#     @staticmethod
#     def func1(a, b):
#         # print(cls)#<class '__main__.myclass'>
#         print(f"a {a} ,b {b}")
#
# obj=myclass()
# obj.func1(1,2)
#
# myclass.func1(1,2)

##############################################################33

# summary

# 3 types of method
# instance-access using obj(instance)
# class-access using obj and classname- standard way to call classmethod using classname(partially forbid)
# static- acess using obj and classname- standard way to call saticmethod using classname(forbid)
