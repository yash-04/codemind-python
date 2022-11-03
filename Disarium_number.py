n=int(input())
c=len(str(n))
t=n
s=0
while n>0:
    r=n%10
    s+=pow(r,c)
    n=n//10
    c-=1
if s==t:
    print(True)
else:
    print(False)