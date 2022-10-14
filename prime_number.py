a=int(input())
c=0
for i in range(2,int(a**0.5)+1):
    if a%i==0:
        print('not a prime')
        c+=1
        break
if c==0:
    print('prime')
    