# private(accessible within the class)(__)
#protected(accessible within class and its derived class)(_)
#public(default)

# public

# class myclass:
#     var="public"
#
#     def func1(self):
#         print("public method")
#         print("inside the public method", self.var)
#
# obj=myclass()
# print(obj.var)
# obj.func1()

#private
# class myclass:
#     __var="private"
#
#     def __func1(self):
#         print("private method")
#         print("inside the private method", self.__var)
#
#     def func2(self):
#         print("public method")
#         print("inside the public method", self.__var)
#         self.__func1()
#
# obj=myclass()
# # print(obj.__var) cannot access private attribute
# # obj.__func1
# obj.func2()


#protected - false protected

class myclass:
    _var="protected"

    def _func1(self):
        print("protected method")
        print("inside the protected method", self._var)




obj=myclass()
print(obj._var)
obj._func1()
