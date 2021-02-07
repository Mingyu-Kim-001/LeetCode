from collections import defaultdict
class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        dp = defaultdict(int)
        dp[0] = 1
        for i in range(1,target+1):
            for num in nums:
                if i-num in dp: dp[i]+=dp[i-num]
        return dp[target]