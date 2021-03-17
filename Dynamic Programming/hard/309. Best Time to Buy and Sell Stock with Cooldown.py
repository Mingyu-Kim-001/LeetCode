class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        dp_0_prev = dp_0_cur = 0
        dp_1 = float("-inf")
        for price in prices:
            temp = dp_0_cur
            dp_0_cur = max(dp_0_cur,dp_1+price)
            dp_1 = max(dp_1,dp_0_prev-price)
            dp_0_prev = temp
        return dp_0_cur