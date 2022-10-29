a,b=map(int,input().split())
c=max(a,b)
i=1
while 1:
    m=c*i
    if m%a==0 and m%b==0:
        print(m)
        break
    i+=1