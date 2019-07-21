import math

pattern="08??840"
total=24
patterns=[]
count=0
countQ=0
for v in pattern:
    if v == '?':
        countQ += 1
        continue
    else:
        count+=int(v)
total -= count
print(total)
totalF = (math.factorial(total)/(math.factorial(countQ)*math.factorial(total-countQ)))-1
i=0
for x in range(int(totalF)):
    j = total
    print(i,j)
    finalpattern = pattern.replace("?", str(i), 1)
    print(finalpattern)
    finalpattern = finalpattern.replace("?", str(j), 1)
    print(finalpattern)
    patterns.append(finalpattern)
    i += 1
    total -= 1
print(patterns)