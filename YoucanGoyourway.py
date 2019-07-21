def path(m):
    matrix = []
    direction = input()
    matrix = [[1 for y in range(m)] for x in range(m)]

    count=0
    for c in direction:
        if count+1<m:
            if c=='E' :
                matrix[count][count+1]=0
            else:
                matrix[count+1][count]=0
            count+=1
    print(matrix)
    j=0
    mylist=[]
    for i in range(m):
        if matrix[i][j]==1 and j!=m-1:
            j+=1
            mylist.append('E')
        else:
            mylist.append('S')
    return mylist




if __name__ == '__main__':
    n = int(input())
    for i in range(n):
        m = int(input())
        mylist=path(m)
    print(mylist)