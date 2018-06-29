#QUESTION 1

f=open ("passage.txt",'r',encoding="UTF8")
n=int(input("enter the number of lines to read"))
list1=f.readlines()
m=len(list1)-n
for i in list1[m:]:
    print(i)

#QUESTION 2
f=open("passage.txt",'r',encoding="UTF8")
freq=input("enter the word to search")
l=f.read()
l1=l.lower()
print(l1.count(freq))


#QUESTION 3
f=open("text.txt","r",encoding="UTF8")
f1=open("passage.txt","a",encoding="UTF8")
for i in f:
    f1.write(i)

#QUESTION 4
f=open("text.txt","r",encoding="UTF8")
f1=open("passage.txt","r",encoding="UTF8")
f2=open("text2.txt","a",encoding="UTF8")
for a ,b in zip(f,f1):
    f2.write(a)
    f2.write(b)


#QUESTION 5

from random import randrange
f=open("text.txt",'w+',encoding='UTF8')
for i in range(10):
    a=randrange(1,11)
    f.write(str(a))



