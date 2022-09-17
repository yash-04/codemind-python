a=int(input())
tem=a
rev=0
while a>0:
    r=a%10
    a=a//10
    rev=rev*10+r
if tem==rev:
    print("True")
else:
    print("False")
