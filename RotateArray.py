def rotate_array(arr,n,d):
    if d>1:
        temp=arr[:2:-1]
        print(temp)
        for i in temp:
            arr.remove(i)
        arr=arr+temp

    return arr


print(rotate_array([1,2,3,4,5],5,2))