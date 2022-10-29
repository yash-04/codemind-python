n=int(input())
l=[0,1]
a,b=0,1
for i in range(1,n-1):
    c=a+b
    a=b
    b=c
    l.append(c)
print(*l)