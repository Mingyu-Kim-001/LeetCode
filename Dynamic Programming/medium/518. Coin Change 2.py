from collections import defaultdict
class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        dp = defaultdict(int)
        dp[0] = 1
        for coin in coins:
            for i in range(1,amount+1):
                if i-coin in dp: dp[i]+=dp[i-coin]
        return dp[amount]