class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        dp_0 = [0] * (k+1)
        dp_1 = [float("-inf")] * (k+1)
        for price in prices:
            for i in range(k,-1,-1):
                dp_0[i] = max(dp_0[i],dp_1[i]+price)
                if i != 0:
                    dp_1[i] = max(dp_1[i],dp_0[i-1]-price)
        return dp_0[k]