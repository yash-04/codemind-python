case=int(input())
for i in range(1,case+1):
    n=int(input())
    a=n+1
    b=n-1
    count=0
    if True:
        for i in range(2,int(n**0.5)+1):
            if n%i==0:
                count+=1
    if count==0:
        print(n)

    else:
        
        while True:
            is_prime=True
            for i in range(2,int(a**0.5)+1):
                if a%i==0:
                    is_prime=False
                    break
            if is_prime==True:
                    break
            else:
                    a+=1

        while True:
            is_prime2=True
            for i in range(2,int(b**0.5)+1):
                if b%i==0:
                    is_prime2=False
                    break
            if is_prime2==True:
                    break
            else:
                    b-=1
        c=a-n
        d=n-b
        if c>d:
            print(b)
        elif d>c:
            print(a)
        else:
            print(b)