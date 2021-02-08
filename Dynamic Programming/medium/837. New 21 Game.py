from collections import defaultdict
class Solution:
    def new21Game(self, N: int, K: int, W: int) -> float:
        #if K==0: return 1
        if N<K: return 0
        result = 0
        dp = defaultdict(int)
        for k in range(K,N+1):
            dp[k] = 1
        S = min(N - K + 1, W)
        for k in range(K-1,-1,-1):
            dp[k] = S/W
            S+= dp[k] - dp[k+W]
        return dp[0]