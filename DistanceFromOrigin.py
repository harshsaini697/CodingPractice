import math
you=[0,0]
post_offices= [[-16, 5], [-1, 2], [4, 3], [10, -2], [0, 3], [-5, -9]]
k = 3
distance1=[]
res=[]
def distancefromyouToPostOffice(you,post_offices,k):
    post_offices.sort(key=lambda K:math.sqrt(math.pow(you[0]-K[0],2) +math.pow(you[0]-K[0],2)))
    return sorted(post_offices[:k])
print(distancefromyouToPostOffice(you,post_offices,k))
