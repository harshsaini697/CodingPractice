

def isunique(s):
    s=s.lower()
    dict={}
    for c in s:
        if(dict.get(c)==1):
            return False
        dict[c]=1
    return True

print(isunique("Harsh"))