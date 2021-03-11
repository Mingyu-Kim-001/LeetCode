#Time: O(n^1.5)
class Solution:
    def numSquares(self, n: int) -> int:
        dp = [float("inf")] * (n+1)
        dp[0] = 0
        i = 1
        perfect_list = []
        while i * i <= n:
            # dp[i*i] = 1
            perfect_list.append(i*i)
            i += 1
        for i in range(1,n+1):
            for perfect in perfect_list:
                if i - perfect >= 0:
                    dp[i] = min(dp[i],dp[i-perfect]+1)
        return dp[n]