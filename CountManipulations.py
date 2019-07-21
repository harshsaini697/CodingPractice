def countManipulations(s1, s2):
    count = 0
    res=[0]*len(s1)
    # store the count of character
    char_count = [0] * 26

    for i in range(26):
        char_count[i] = 0

    # iterate though the first String
    # and update count
    for j in range(len(s1)):
        if len(s1[j])!=len(s2[j]):
            res[j]=-1
            continue
        for i in range(len(s1[j])):
            char_count[ord(s1[j][i]) -
                       ord('a')] += 1

    # iterate through the second string
    # update char_count.
    # if character is not found in
    # char_count then increase count

        for b in range(len(s2[j])):
            char_count[ord(s2[j][b]) - ord('a')] -= 1
            if (char_count[ord(s2[j][b]) -
                       ord('a')] < 0):
                count += 1
        res[j]=count
    return res


# Driver code
if __name__ == "__main__":
    s1 = ["a","jk","abb","xaxbbx"]
    s2 = ["bb","kj","bbc","xaxqqa"]
    print(countManipulations(s1, s2))