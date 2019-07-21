#Find the largest pair sum in an unsorted array
#Given an unsorted of distinct integers, f
# find the largest pair sum in it. For example,
# the largest pair sum in {12, 34, 10, 6, 40} is 74.
arr=[12, 34, 10, 6, 40]
max=float('-inf')
def findLargestSum(arr):
    if arr[0]>arr[1]:
        first=arr[0]
        second=arr[1]
    else:
        first=arr[1]
        second=arr[0]

    for i in range(2,len(arr)):
        if arr[i]>first: #distinct elements hence cannot be equal
            second = first
            first=arr[i]
        elif first>arr[i]>second :
            second=arr[i]
    return first+second

print(findLargestSum(arr))

