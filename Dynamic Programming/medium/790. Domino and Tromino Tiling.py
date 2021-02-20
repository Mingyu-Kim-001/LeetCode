#Time: O(n)
class Solution:
    def numTilings(self, N: int) -> int:
        MOD = pow(10,9) + 7
        dp = [0]*(N+1)
        dp[0] = 1
        prefix = 0
        for i in range(1,N+1):
            if i>=3:prefix+=dp[i-3]
            dp[i] = dp[i-1] + dp[i-2] + (2*prefix if i>=3 else 0)
        return dp[N]%MOD