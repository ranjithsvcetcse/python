# Enter your code here. Read input from STDIN. Print output to STDOUT
def is_prime(n):
    c=0
    for i in range(1,n+1):
        if n%i==0:
            c=c+1
        if c==3:
            return False
    if c==2:
        return True
    else:
        return 'Error'

a=int(input())
if is_prime(a):
    print(a,"is prime")
else:
    print(a,"is not prime")
