#f=open("text.txt",'r')
#print(f)
#print(f.read())
#print(f.readline())
#print(f.readline())

#print(f.readlines())

"""
f=open("text.txt",'w')
f.write("hello\n")
#f.write("mr.")
"""
f=open("text.txt",'w')
l=["a\n","b\n","c\n"]
f.writelines(l)

with open("text.txt",'r') as f:
    #f.read()
    #f.readlines()

    print(f.read(5))
    print(f.tell())

    f.seek(0)
    print(f.tell())

#f1.write(f2) to combine file
#4 readline
#5 import random
#random.rand
#make list and sort it


