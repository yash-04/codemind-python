def is_prime(m):
    if m<2:
        return False
    for i in range(2,int(m**0.5)+1):
        if m%i==0:
            return False
    return True

def run_loop_till_prime(n,x):
    while is_prime(n)==False:
        n+=x
    return n
t=int(input())
for i in range(1,t+1):
    n=int(input())
    pp=run_loop_till_prime(n,-1)
    np=run_loop_till_prime(n,1)
    a=abs(n-pp)
    b=abs(n-np)
    if a>b:
        print(np)
    elif b>a:
        print(pp)
    else:
        print(pp)