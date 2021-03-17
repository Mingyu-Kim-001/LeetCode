#Time: O(n), Space: O(1)
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        dp_0,dp_1 = 0,float("-inf")
        for price in prices:
            tmp_dp_0 = dp_0
            dp_0 = max(dp_0,dp_1+price)
            dp_1 = max(dp_1,tmp_dp_0-price)
        return dp_0
    
    #dp_0[i] : the maximum profit on ith day having no stock
    #dp_1[i] : the maximum profit on ith day having one stock
    #dp_0[i] = max(dp_0[i-1],dp_1[i-1]+price)
    #dp_1[i] = max(dp_1[i-1],dp_0[i-1]-price)