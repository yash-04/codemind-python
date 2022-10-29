a=int(input())
s=0
b=a*a
while b>0:
    r=b%10
    s+=r
    b=b//10
if s==a:
    print('Neon Number')
else:
    print("Not Neon Number")