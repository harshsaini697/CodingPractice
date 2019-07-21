def StringCompreession(str1):
    count=0
    i=0
    oldvalue=''
    fin=''
    while i <len(str1):
        oldvalue = str1[i]
        count=1
        i+=1
        while(i<len(str1) and str1[i]==oldvalue ):
            count+=1
            i+=1
        fin=fin+oldvalue+str(count)
        count=0

    return fin
print(StringCompreession("aabcccca"))