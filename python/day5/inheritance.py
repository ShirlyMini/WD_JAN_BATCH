# class parent /base / super
#class child / derived /sub class

# types 5
# single inher

# class parent:
#     def func1(self):
#         print("this is the func1 from parent class")
#
# class child(parent):
#     def func2(self):
#         print("this is the func2 from child class")
#
# obj_p=parent()
# obj_p.func1()
#
# obj = child()
# obj.func1()
# obj.func2()

##############################################################33
# multiple inhert
# class parent1:
#     def func1(self):
#         print("this is the func1 from parent1 class")
#
# class parent2:
#     def func3(self):
#         print("this is the func3 from parent2 class")
#
# class child(parent1, parent2):
#     def func2(self):
#         print("this is the func2 from child class")
#
# obj = child()
# obj.func1()
# obj.func2()
# obj.func3()

####################################################333
# multilevel

# class parent1:
#     def func1(self):
#         print("this is the func1 from parent1 class")
#
# class parent2(parent1):
#     def func3(self):
#         print("this is the func3 from parent2 class")
#
# class parent3(parent2):
#     def func4(self):
#         print("this is the func4 from parent3 class")
#
# class child(parent3):
#     def func2(self):
#         print("this is the func2 from child class")
#
# obj=child()
# obj.func1()
# obj.func2()
# obj.func3()
# obj.func4()

#################################################################3
# hierarchial

# class parent1:
#     def func1(self):
#         print("this is the func1 from parent1 class")


# class child1(parent1):
#     def func2(self):
#         print("this is the func2 from child1 class")
#
# class child2(parent1):
#     def func3(self):
#         print("this is the func2 from child2 class")
#
# obj_a=child1()
# obj_a.func1()
# obj_a.func2()
#
# obj_b=child2()
# obj_b.func1()
# obj_b.func3()


#########################################################33
# hybrid

class parent1:
    def func1(self):
        print("this is the func1 from parent1 class")

class parent2(parent1):
    def func4(self):
        print("this is the func1 from parent1 class")

class parent3(parent2):
    def func5(self):
        print("this is the func1 from parent1 class")


class child1(parent3):
    def func2(self):
        print("this is the func2 from child1 class")


class child2(parent3):
    def func3(self):
        print("this is the func2 from child2 class")


obj_a = child1()
obj_a.func1()
obj_a.func2()
obj_a.func4()
obj_a.func5()

obj_b = child2()
obj_b.func1()
obj_b.func3()
obj_b.func4()
obj_b.func5()