
def isPalindrome( x: int) -> bool:
    if (x < 0 or (x % 10 == 0 and x != 0)):
        return False
    reverted = 0
    while (x > reverted):
        reverted = reverted * 10 + x % 10
        x /= 10
        x=int(x)

    return (x == reverted or x == reverted / 10)


isPalindrome(121)