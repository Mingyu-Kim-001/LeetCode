class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        dp_0 = [0] * 3
        dp_1 = [float("-inf")] * 3
        for price in prices:
            for i in range(2,-1,-1):
                dp_0[i] = max(dp_0[i],dp_1[i]+price)
                if i != 0:
                    dp_1[i] = max(dp_1[i],dp_0[i-1]-price)
        return dp_0[2]