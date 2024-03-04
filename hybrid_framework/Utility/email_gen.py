import string
import random

print(string.ascii_letters)
print(string.digits)
print(random.choice(string.ascii_letters+string.digits))
# list1=[]
# for i in range(8):
#     list1.append(random.choice(string.ascii_letters + string.digits))
# print(list1)
# list1=[random.choice(string.ascii_letters + string.digits) for i in range(8)]
print("".join([random.choice(string.ascii_letters + string.digits) for i in range(8)]))