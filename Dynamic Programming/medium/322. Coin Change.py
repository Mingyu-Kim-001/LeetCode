#Time: O(n)
from collections import defaultdict
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = defaultdict(lambda: float("inf"))
        dp[0] = 0 #dp[i] is the fewest number of coins to make i
        for i in range(1,amount+1):
            for coin in coins:
                dp[i] = min(dp[i-coin]+1,dp[i])
        return dp[amount] if dp[amount]!=float("inf") else -1