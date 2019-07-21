
def find(n):
    m=int( input())
    if(m%2 == 1 ) :
        x,y=m+ 1 / 2 , m - 1/ 2
        return x,y
    else:
        x,y=m/ 2 , m / 2
        return x,y

if __name__=='__main__' :
    n=int(input())
    for i in range(n):
        x,y=find(n)
        print(int(x),int(y))