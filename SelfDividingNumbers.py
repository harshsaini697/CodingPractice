def selfDividingNumbers( left: int, right: int):
    res = []
    for i in range(left, right + 1, 1):
        flag = False
        j = i
        while (i >= 1):
            temp = i % 10
            if (temp != 0 and j % temp == 0):
                i = int(i / 10)
                flag = True
            else:
                flag=False
                break

        if flag == True:
            res.append(j)
    return res

print(selfDividingNumbers(20,22))


