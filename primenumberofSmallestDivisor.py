import math
def prime(n):
    if n >1:
        for i in range(2,n//2):
            if n%i==0:
                return False
            else:
                return True
    else:
        return False

def smallestDivisor(n):
    if n<=1:
        return n
    if n%2==0:
        return 2
    if n%3==0:
        return 3
    for i in range(5,math.sqrt(n),6):
        if n%i==0:
            return i
        elif(n%(i+2)==0):
            return i+2
    return n



    pass

if __name__=="__main__":
    n=int(input())
    if prime(n):
        print("Prime")
    else:
        print(smallestDivisor(n))


