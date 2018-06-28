#QUESTION 1

print("the exception occured is ZeroDivisionError exception ")
try:
    a=3
    if a<4:
        a=a/(a-3)
        print(a)
except ZeroDivisionError:
    print("can not divide by zero, please enter a number greater than 3 or less than 3 ")
else:
    print("the value a is ,a")


#QUESTION 2

print("the exception occured is IndexError")

try:
    l=[1,2,3]
    l1=l[3]
    print(l1)
except IndexError:
    print("please enter a valid index i.e less than 3")
else:
    print("the value of list is",l1)


#QUESTION 3

try:
    raise NameError("Hi there")
except NameError:
    print ("An exception")


#QUESTION 4

def AbyB(a , b):
	try:
		c = ((a+b) / (a-b))
	except ZeroDivisionError:
		print ("a/b result in 0")
	else:
		print(c)

AbyB(2.0, 3.0)
AbyB(3.0, 3.0)


#QUESTION 5

#ImportError

try:
    import rawat
except ImportError:
    print("import file dosesnt exist")

#value error
try:
    a=int(input("enter a number"))
except ValueError:
    print("please enter a valid number")
else:
    print(a)

#Index error

try:
    a=[1,2,3,4]
    b=a[5]
    print(b)
except IndexError:
    print("please enter a index less than 5")
else:
    print("value of list is ",b)


#QUESTION 6

class AgeTooSmall(Exception):
    pass
value=True
while value:
    try:
        a=int(input("enter age"))
        if a<18:
            raise AgeTooSmall
    except ValueError:
        print("please enter age in integer")
    except AgeTooSmall:
        print("your age is less than 18")
    else:
        print("you are eligible")
        value=False
