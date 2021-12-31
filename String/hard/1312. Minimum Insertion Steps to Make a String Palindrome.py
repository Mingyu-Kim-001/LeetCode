class Solution:
    def minInsertions(self, s: str) -> int:
        n = len(s)
        dp = [[0] * (n + 1) for _ in range(n + 1)]
        for i in range(1, n + 1):
            for j in range(1, n + 1):
                dp[i][j] = dp[i-1][j-1] + 1 if s[i-1] == s[-j] else max(dp[i-1][j], dp[i][j-1])
        return n - dp[n][n]