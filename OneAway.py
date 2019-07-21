def OneAway(str1,str2):
    if abs(len(str1)-len(str2)) >1:
        return False
    count=0

    m=len(str1)
    n=len(str2)
    i=0
    j=0

    while i < m and j < n:
        # If current characters dont match
        if str1[i] != str2[j]:
            if count == 1:
                return False

            # If length of one string is
            # more, then only possible edit
            # is to remove a character
            if m > n:
                i += 1
            elif m < n:
                j += 1
            else:  # If lengths of both strings is same
                i += 1
                j += 1

            # Increment count of edits
            count += 1

        else:  # if current characters match
            i += 1
            j += 1

        # if last character is extra in any string
    if i < m or j < n:
        count += 1

    return count==1

print(OneAway("pale","paale"))