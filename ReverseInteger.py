def reverseinteger(n:int):
    rev=0
    flag=False
    if n<0:
        flag=True
        n*=-1
    while(n!=0):
        pop=n%10
        n=int(n/10)
        if (rev > float('inf') / 10 or  (rev == float('inf')/ 10 and pop > 7)):
            return 0
        if (rev < float('-inf') / 10 or  (rev == float('-inf')/ 10 and pop <-8)):
            return 0
        rev=rev*10+pop
    if flag==True:
        rev*=-1
    return rev

print(reverseinteger(-123))


