import math
def sum(a,b):
    return a+b
def sub(a,b):
    return a-b
def mul(a,b):
    return a*b
def div(a,b):
    return a/b
def root(a):
    return math.sqrt(a)
while True:
    a=int(input("Enter the first no.:"))
    b=int(input("Enter the second no.:"))
    c=input("Enter the operator:")
    if(c=='+'):
        print("The sum of two no. is:",sum(a,b))
    elif(c=='-'):
        print("The subtraction of two no. is:",sub(a,b))
    elif(c=='*'):
        print("The multiplication of two no. is:",mul(a,b))
    elif(c=='/'):
        print("The division of two no. is:",div(a,b))
    elif(c=='root'):
        print("The root of the first number is:",root(a))
    else:
        print("Invalid operator !")
        break