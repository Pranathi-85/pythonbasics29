""""##alternative fib series in a range
a=0
b=1
c=0
x=int(input("enter number"))
y=int(input("enter number"))
for i in range(x,y+1):
    if (c%2==0):
        print(a)
    c=a+b
    a=b
    b=c
c=+1
"""

##fib series in prime numbers
def isprime(x):
    for i in range(2,x):
        if(x%i==0):
            return False
    return True
g=int(input("enter number"))
h=int(input("enter number"))
a=0
b=1
for i in range(g,h+1):
    if (isprime(i)):
        print(a)
    c=a+b
    a=b
    b=c
