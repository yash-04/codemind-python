n=int(input())
p=0
for i in range(1,int(n/2)+1):
    if n%i==0:
        p+=i
if p==n:
    print('True')
else:
    print('False')
        