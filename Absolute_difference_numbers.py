N,X=map(int,input().split())
t=N
rev=s=0
r1=N%(10**X)
while t>0:
    r2=t%10
    t=t//10
    rev=rev*10+r2
r3=rev%(10**X)
while r3>0:
    r4=r3%10
    r3=r3//10
    s=s*10+r4
print(abs(r1-s))
    
