# print(a)#NameError
# syntax and exceptions()
# if condt:
#     print("true")#SyntaxError and IndentationError
# import builtins
# print(dir(builtins))

# print("statement1")
# print("statement1")
# print("statement1")
# print("statement1")
# print("statement1")
# try:
#     print(a)# program is getting terminated # type error
# except:
#     print("exception happened")
# print("statement2")
# print("statement2")
# print("statement2")
# list1=[1,2,3,4]
# try:
#     # print("a"+10)# program is getting terminated # type error
#     print(list1[4])
# except NameError as msg:# Exception will catch all kind of exception
#     print("exception happened Name", msg)
# except TypeError as msg:# Exception will catch all kind of exception
#     print("exception happened Type", msg)
# except Exception as msg:# Exception will catch all kind of exception
#     print("exception happened", msg)

# optional blocks
# else(if no exception)
# finally(always get execute)
# list1=[1,2,3,4]
# try:
#     print(list1[3])
# except Exception as msg:
#     print("exception happened", msg)
# else:
#     print("No Exception happened")
# finally:
#     print("finally block executed")

######################3
# user defined error
######################3
# raise

# try:
#     n=22
#     if n>=18:
#         print("eligible for vote")
#     else:
#         raise Exception("Not eligible for vote")#Exception: Not eligible for vote
# except Exception as e:
#     print(e)

# assert

# assert True# proceed
# assert False, "this is user generated"# thow the assertionerror
# try:
#     n=22
#     assert n>=18, "Not eligible for vote"
#     print("eligible for vote")#AssertionError: Not eligible for vote
# except Exception as e:
#     print(e)