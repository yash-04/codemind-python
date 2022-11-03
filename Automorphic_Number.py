n=int(input())
c=str(n)
m=n*n
i=10
a=len(c)
while a>0:
    r=m%i
    if r==n:
        print('Automorphic Number')
        break
    else:
        i*=10
        a-=1
if(a==0):
      print('Not an Automorphic Number')
        
    