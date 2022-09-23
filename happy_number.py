a=int(input())
s=0
while a>0:
    r=a%10
    a=a//10
    s+=r*r
    if a==0 and s>9:
        a=s
        s=0
if s==1 or s==7:
    print("True")
else:
    print("False")