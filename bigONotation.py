#big o -> n
def bigon(n):
    for i in range(0,n):
        print(i)
bigon(5)

#big o -> logn
import math
def logn(n):
    while n > 1:
        n = math.floor(n/2)
        print(n)
logn(5)

#big o -> nlogn
def nfactorial(n):
    if n == 0:
        print("1")
        return
    else:
        for i in range(0,n):
            print(i)
            nfactorial(n-1) #recursive function
nfactorial(6)