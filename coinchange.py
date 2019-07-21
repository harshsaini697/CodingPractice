def coinChange( coins, amount: int) -> int:
    dp = [0] * (amount + 1)
    for i in range(1, amount + 1):
        dp[i] += min(((dp[i - j]) for j in coins if i >= j and dp[i - j] >= 0), default=-2) + 1
    return dp[amount]



def coinWays(coins,amount):
    dp = [0] * (amount + 1)
    dp[0]=1
    for i in coins:
        for j in range(i,len(dp)):
            dp[j]+=dp[j-i]
    return dp[amount]

print(coinWays([1,2,3],4))