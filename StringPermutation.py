
def stringPermutation(st1,st2):
    count1=[0]*256
    count2=[0]*256
    if len(st1)!=len(st2):
        return "No"
    for c in st1:
        count1[ord(c)]+=1
    for c in st2:
        count2[ord(c)]+=1

    for i in range(256):
        if(count1[i]!=count2[i]):
            return "No"
    return "Yes"

print(stringPermutation("harsh","sharh"))