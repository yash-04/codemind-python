a=int(input())
d=0
while a>0:
    n=a%10
    a=a//10
    if n>d:
        d=n
print(d)