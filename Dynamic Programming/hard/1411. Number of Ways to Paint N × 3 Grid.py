class Solution:
    def numOfWays(self, n: int) -> int:
        dp = []
        MOD = (pow(10,9)+7)
        for i in range(n):
            dp.append([0,0])
        dp[0][0] = dp[0][1] = 6
        for i in range(1,n):
            dp[i][0] = (3*dp[i-1][0] + 2*dp[i-1][1])%MOD
            dp[i][1] = (2*sum(dp[i-1]))%MOD
        return sum(dp[n-1])%MOD
#         A : 6 - A3B2
#         B : 6 - A2B2
        