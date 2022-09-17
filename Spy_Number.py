a=int(input())
s=0
p=1
while a>0:
    n=a%10
    a=a//10
    s+=n
    p*=n
if s==p:
    print("Spy Number")
else:
    print("Not Spy Number")
