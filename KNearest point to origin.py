import math
arr=[
    [-1,0],
    [0,-2],
    [3,2],
    [-2,4],
    [3,5]
]
newlist=[]
mylist=[]
for i in arr:
    x=i[0]
    y=i[1]
    d=math.sqrt(x**2 + y**2)
    newlist.append(d)
k=5
for i in range(k):
    lol=arr[newlist.index(min(newlist))]
    newlist.pop(arr.index(lol))
    arr.remove(lol)
    print(lol)
    mylist.append(lol)

