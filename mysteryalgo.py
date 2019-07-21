
def mystery(x,y):
    if(x>y):
        x=x-y
    if(x<y):
        y=y-x
    return x, y

if __name__ == '__main__':
    x = 2437
    y = 875
    while(x!=y):
        x, y = mystery(x, y)
        print(x,y)