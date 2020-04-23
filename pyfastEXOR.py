from sys import stdin, stdout 
t = stdin.readline()
t = int(t)
while t>0:
    N,Q = list(map(int,stdin.readline().split()))
    A= stdin.readline()
    list1=list(map(int,A.split()))
    for i in range (0 , Q):
        query=int(stdin.readline())
        liste=[]
        listo=[]
        for k in range(0,N):
            res = (query)^(list1[k])
            resb=bin(res).replace("0b", "")
            b = int(resb)
            c = 0
            while (b > 0):  
              if (b % 10 == 1): 
                  c += 1; 
              b = int(b / 10)
            if c%2==0:
                liste.append(c)
            else:
                listo.append(c)    
                
    stdout.write(str(len(liste))),stdout.write(' '),stdout.write(str(len(listo)))
    
    t = t - 1