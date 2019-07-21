def lengthOfLongestSubstring( s: str) -> int:
    i = 0
    ans = 0
    mydict = {}
    for j in range(len(s)):
        if s[j] in mydict:
            i = max(mydict[s[j]], i)
        ans = max(ans, j - i + 1)
        mydict[s[j]] = j + 1
    return ans


s="dvdf"
print(lengthOfLongestSubstring(s))