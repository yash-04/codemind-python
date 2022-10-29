n=int(input())
a,b=0,1
l=[0,1]
for i in range(1,n):
    c=a+b
    a=b
    b=c
    l.append(c)
if n in l:
    print(True)
else:
    print(False)