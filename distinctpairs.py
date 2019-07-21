def distinct(arr,n,k):
    count=0
    hashmap={}
    for x in arr:
        hashmap[x] = 1
    for i in arr:
        a=i
        if hashmap[k-a] >= 0:
            if hashmap[k-a] == 1:
                count+=1
            else:
                continue
        hashmap[x]= 0
    print(count)

if __name__ == '__main__':
    arr=[1,2,3,6,7,8,9,1]
    n=len(arr)
    k=10
    distinct(arr,n,k)





