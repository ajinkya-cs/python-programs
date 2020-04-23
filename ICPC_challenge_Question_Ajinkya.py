""" WinxToshiba ...Py
 Ajinkya29 """


from collections import Counter 
from math import factorial
def funcnc(n, r): 
    return ((factorial(n) // (factorial(r)  
                * factorial(n - r)))) 
def exo(a,b):
    return a^b
    
T=int(input())
for it in range(T):
    N=int(input())
    A=[int(i) for i in input().split(" ")]
    Q=int(input())
    for j in range(Q):
        L,R=[int(i) for i in input().split(" ")]
        
        ll=A[L-1:R]
        count=dict(Counter(ll))
        ans=list(count.values())
        xor=0
        for i in ans:
            xor=exo(xor,i)
        if xor == 0:
            print("0")
        else:
            aturn=0
            for k in ans:
                n=k
                r=exo(xor,k)
                if n > r:
                    aturn+=funcnc(n,r)
            print(aturn%998244353)
