# read(default)
# write
#append-

# with open("test1.txt", "w") as FH:
#     FH.write("this is statement4\n")
#     FH.write("this is statement5\n")
#     FH.write("this is statement6\n")


# with open("test1.txt", "a") as FH:
#     FH.write("this is statement4\n")
#     FH.write("this is statement5\n")
#     FH.write("this is statement6\n")

with open("test1.txt") as FH:
    # print(FH.read())# whole content
    # print(FH.readline())# to read signgle line
    # print(FH.readline())
    # print(FH.readline())
    # print(FH.readline())
    # print(FH.readline())
    # print(FH.readline())
    print(FH.readlines())# all lines in list