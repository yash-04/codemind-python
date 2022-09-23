n=int(input())
sq_1=n*n
s=s2=0
while n>0:
    r=n%10
    n=n//10
    s=s*10+r
sq_2=s*s
t=sq_2
while t>0:
    r2=t%10
    t=t//10
    s2=s2*10+r2
if sq_1==s2:
    print('True')
else:
    print('False')