def getIndexPositions(listOfElements, element):
    indexPosList = []
    indexPos = 0
    while True:
        try:
            indexPos = listOfElements.index(element, indexPos)
            indexPosList.append(indexPos)
            indexPos += 1
        except ValueError as e:
            break
 
    return indexPosList
def getvalue(indexPosList,prices):
    answer=0
    for i in indexPosList:
        answer=answer+prices[i]
    return answer

t = int(input())
while t>0:
    N,M = list(map(int,input().split()))
    fruits=list(map(int,input().split()))
    prices=list(map(int,input().split()))
    price=0
    ans = 0
    pricelist=[]
    for k in range(0,N):
        element1 = fruits[k]
        indexlist = getIndexPositions(fruits,element1)
        price = getvalue(indexlist,prices)
        pricelist.append(price)
    pricelist.sort()
    if pricelist[0] != 0:
        ans = pricelist[0]
    else :
        for k in range (1,N):
            if pricelist[k]!=0:
                ans = pricelist[k]
                break
            
            
    print(ans)    
    
    
    t = t-1