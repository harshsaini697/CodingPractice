# def PalindromePermutation(str1):
#     count=0
#     str1 = str1.replace(' ', '').lower()
#     if len(str1)%2 ==0:
#         count=1
#     return True

from collections import Counter


def PalindromePermutation(data: str) -> bool:
    """Given a string, check if it is a permutation of a palindrome."""
    data = data.replace(' ', '').lower()
    return sum(freq%2 for freq in Counter(data).values())<2

print(PalindromePermutation(""))