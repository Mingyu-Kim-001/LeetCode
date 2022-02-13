class Solution:
    def rearrangeSticks(self, n: int, k: int) -> int:
        #dp[i][j] = rearrangeSticks(i, j)
        dp = [[0] * (k + 1) for _ in range(n + 1)]
        dp[1][1] = 1
        MOD = pow(10, 9) + 7
        for i in range(2, n+1):
            for j in range(1, min(k+1, i+1)):
                dp[i][j] = dp[i-1][j-1]
                if i - 1 >= j:
                    dp[i][j] += dp[i-1][j] * (i-1)
                    dp[i][j] %= MOD
        return dp[n][k]