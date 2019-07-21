def deviation(mylist,k):
    n=len(mylist)
    median=0
    for i in range(0,n-k+1):
        min=float('+inf')
        max=float('-inf')
        for j in range(i,i+k):
            if mylist[j]<min:
                min=mylist[j]
            if mylist[j]>max:
                max=mylist[j]

        if median<max-min:
            median=max-min
    return median

print(deviation([6,9,4,7,4,1,6,9,4,7,4,1,6,9,4,7,4,1,6,9,4,7,4,16,9,4,7,4,1,6,9,4,7,4,1,6,9,4,7,4,1,6,9,4,7,4,1,6,9,4,7,4,1,6,9,4,7,4,1,6,9,4,7,4,1,6,9,4,7,4,1,6,9,4,7,4,1,6,9,4,7,4,1]))