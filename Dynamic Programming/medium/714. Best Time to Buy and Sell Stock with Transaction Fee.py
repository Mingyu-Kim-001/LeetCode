#Time: O(n), space: O(1)
class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        dp_i1 = float("-inf")
        dp_i0 = 0
        for price in prices:
            tmp_dp_i0 = dp_i0
            dp_i0 = max(dp_i0,dp_i1+price-fee)
            dp_i1 = max(dp_i1,tmp_dp_i0-price)
        return dp_i0