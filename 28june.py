"""
#1
try:
    a=0
    b=3/0
except ZeroDivisionError:
    print("number is divided by 0 ")
else:
    print(a)

finally:
    print("i will execute")
"""
# 2
try:

    a=[1,2,3]
    print(a[3])
except ZeroDivisionError:

    print("no. is divided by 0")
except IndexError:
    print("index dosnt exit")

import rawat
except ImportError:
    print("import file dosesnt exist")
"""
# 3
class AgeError(Exception):
    pass
try:
    a=int(input("enter age"))
    if(a<18):
        raise AgeError
except ValueError:
    print("please enter integer")
except AgeError:
    print("you are under age")
else:
    print("you are eligible")

try:
    raise NameError("hi there")
except NameError:
    print (" an exception")
"""