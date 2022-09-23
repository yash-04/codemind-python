n=int(input())
s=0
if n>0:
    while n>0:
        r=n%10
        n=n//10
        s=s*10+r
    print(s)
else:
    n=n*(-1)
    while n>0:
        r=n%10
        n=n//10
        s=s*10+r
    print(-s)
