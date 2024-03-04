# def is keyword
# create
# call

# def myfunc():
#     print("this is the statement")
#     return True

# myfunc()
# print(myfunc)# reference of the funct
# print(myfunc())

# var = myfunc
# print(var())


###############
# two types of parameter / argume
# postional
# keyword
# def addition(a,b,c,d):
#     print(f"a{a}+b{b}+c{c}+d{d}={a+b+c+d}")
# postional para
# addition(1,2,3)#TypeError: addition() missing 1 required positional argument: 'd'
# addition(1,2,3, 4)# eg for posti
# addition(1,2,3, 4,5)#TypeError: addition() takes 4 positional arguments but 5 were given

# keyword para
# addition(a=2, b=1, c=4, d=5)# keyword part
# addition(b=1, a=2, d=5,c=4)# keyword part
# addition(b=1, a=2, d=5)# TypeError: addition() missing 1 required positional argument: 'c'

# addition(1,2,c=10,d=20)
# addition(1,2,c=10,b=20)#TypeError: addition() got multiple values for argument 'b'
# addition(a=1,b=2, 3,4)#SyntaxError: positional argument follows keyword argument


# def addition(a,b,c=0,d=0):# default parameter
#     print(f"a{a}+b{b}+c{c}+d{d}={a+b+c+d}")

# addition(1,2,3, 4)
# addition(1,2,3)
# addition(1,2)
# addition(1)#TypeError: addition() missing 1 required positional argument: 'b'

# addition(a=1,b=2,c=3, d=4)
# addition(a=1,b=2, d=4)

# addition(1,2,c=3,d=4)
# addition(1,2,c=3,d=4)


############################################################
# with para with return

# def myclass(name):
#     return f"Hello, {name}"
#
# print(myclass("shirly"))

# without para with return
# def myclass():
#     name="shirly"
#     return f"Hello, {name}"
#
# print(myclass())

# with para without return

# def myclass(name):
#     print(f"Hello, {name}")
#     # return # None
#
# print(myclass("shirly"))

# without para without return

# def myclass():
#     name="shirly"
#     print(f"Hello, {name}")
#
# myclass()

###########################################################

# local
# global


# var1="global"

# def myfunc(var3):
#     var2="local"
#     print(f"variables inside func var1{var1} and var2{var2} and var3{var3}")

# print(f"variables outside func before calling myfunc var1{var1} and var2{var2} and var3{var3}")
# myfunc("para_local")
# print(f"variables outside func after calling myfunc var1{var1} and var2{var2} and var3{var3}")


############################################################3
#ex1

# a="global"
#
# def myfunc():
#     # print(f"inside func before initiating a {a}")#UnboundLocalError: cannot access local variable 'a' where it is not associated with a value
#     #SyntaxError: name 'a' is used prior to global declaration
#     global a
#     a="local"
#     print(f"inside func a {a}")
#
# print(f"outside func before calling myfunc a {a}")
# myfunc()
# print(f"outside func after calling myfunc a {a}")

##############################################################

#*args and **kwargs

# def add(*var):
#     print(var)#(1, 2, 3, 4, 5, 6, 7, 8, 9)
#     sum=0
#     for i in var:
#         sum=sum+i
#     return sum
#
#
# print(add(1,2,3,4,5,6,7,8,9,10,20,30))


# def add(**var):
#     print(var)#{'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6, 'g': 7, 'h': 8, 'i': 9}
#     print(var.values())
#     sum=0
#     for i in var.values():
#         sum=sum+i
#     return sum
#
#
# print(add(a=1,b=2,c=3,d=4,e=5,f=6,g=7,h=8,i=9))


def add(*agrs, **kwagrs):
    print(agrs)# tup
    print(kwagrs)# dict

    sum=0
    for i in agrs:
        sum=sum+i
    for j in kwagrs.values():
        sum=sum+j
    return sum

print(add(1,2,3,4, a=1,b=2,c=3,d=4, e=100))
