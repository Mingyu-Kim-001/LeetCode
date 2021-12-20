from collections import defaultdict
class Solution:
    def findTargetSumWays(self, nums: List[int], S: int) -> int:
        dp = defaultdict(int)
        dp[0] = 1
        for num in nums:
            dp2 = defaultdict(int)
            for i in dp:
                dp2[i+num]+=dp[i]
                dp2[i-num]+=dp[i]
            dp = dp2
        return dp[S]