# modules= collection of func and class

# import module1
# import module2
#
# module1.printer1()
# module2.printer2()
#
# module1.printer3()
# module2.printer3()
#
# obj=module1.A()
# obj.func1()
#
# obj=module2.B()
# obj.func1()
# ####################################33
#
# from module1 import printer1,printer3, A#*
# from module2 import printer2,printer3, B#*
#
# printer1()
# printer2()
# printer3()# from mod 2(latest import)

# package
#external package-selenium,request(api),excel openpyxl ,pandas
# internal package - math, sys, os,
# custom package

# from pack1.module1 import *
#
# printer1()
# printer3()
# obj=A()
# obj.func1()

# from pack1 import module1
#
#
# module1.printer1()
# module1.printer3()
# obj=module1.A()
# obj.func1()

from pack1.pack2 import module2

module2.printer3()
module2.printer2()
obj = module2.B()
obj.func1()
